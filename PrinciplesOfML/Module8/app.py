from flask import Flask, request, jsonify, render_template
from datetime import datetime, timedelta
import pandas as pd
import requests
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import spacy
from azure.core.credentials import AzureKeyCredential
from azure.maps.search import MapsSearchClient
import numpy as np

app = Flask(__name__)

SUBSCRIPTION_KEY = '6Hk0BuzXAh248HIBaBisjFdj0Y7bi97o09bOZMSyakK7IVyu9zSLJQQJ99AGAC8vTInLFAINAAAgAZMP9xmM'
# Initialize spaCy
nlp = spacy.load("en_core_web_sm")

# Define the columns to use
selected_columns = ['temperature_min', 'temperature_max', 'temperature_avg', 'precipitation', 'snowfall', 'snow_depth', 'heating_degree_days', 'cooling_degree_days']

# Initialize the scaler and KMeans model
scaler = MinMaxScaler()
kmeans = KMeans(n_clusters=4)

# Define a list of trails with their suitable conditions
trails = [
    {
        'name': 'Sunnyvale Bay Trail',
        'min_temp': 10,
        'max_temp': 30,
        'max_precipitation': 1,
        'description': 'A scenic trail along the bay with moderate difficulty.'
    },
    {
        'name': 'Mission Peak Trail',
        'min_temp': 15,
        'max_temp': 25,
        'max_precipitation': 0.5,
        'description': 'A challenging hike with a great view from the top.'
    },
    {
        'name': 'Alum Rock Park',
        'min_temp': 12,
        'max_temp': 28,
        'max_precipitation': 2,
        'description': 'A family-friendly trail with picnic areas and wildlife.'
    }
]

def search_address(query):
    maps_search_client = MapsSearchClient(credential=AzureKeyCredential(SUBSCRIPTION_KEY))
    result = maps_search_client.search_address(query=query)
    if len(result.results) > 0:
        lat = result.results[0].position.lat
        lon = result.results[0].position.lon
        return lat, lon
    else:
        return None, None

def fetch_weather_data(lat, lon, start_date, end_date):
    params = {
        'api-version': '1.1',
        'query': f"{lat},{lon}",
        'startDate': start_date.strftime('%Y-%m-%d'),
        'endDate': end_date.strftime('%Y-%m-%d'),
        'subscription-key': SUBSCRIPTION_KEY,
    }
    max_retries = 10
    retry_count = 0
    while retry_count < max_retries:
        try:
            response = requests.get("https://atlas.microsoft.com/weather/historical/actuals/daily/json", params=params)
            if response.status_code == 200:
                return response.json()
            else:
                retry_count += 1
                if retry_count < max_retries:
                    time.sleep(10)  # Wait for 10 seconds before retrying
                else:
                    return None
        except requests.exceptions.ConnectionError:
            retry_count += 1
            if retry_count < max_retries:
                time.sleep(10)  # Wait for 10 seconds before retrying
            else:
                return None
    return None

def preprocess_data(raw_data, location_name):
    processed_data = []
    for day_data in raw_data['results']:
        try:
            processed_data.append({
                'location_name': location_name,
                'timestamp': datetime.strptime(day_data['date'], '%Y-%m-%dT%H:%M:%S%z'),
                'temperature_min': day_data['temperature']['minimum']['value'],
                'temperature_max': day_data['temperature']['maximum']['value'],
                'temperature_avg': day_data['temperature']['average']['value'],
                'precipitation': day_data['precipitation']['value'],
                'snowfall': day_data['snowfall']['value'],
                'snow_depth': day_data['snowDepth']['value'],
                'heating_degree_days': day_data['degreeDaySummary']['heating']['value'],
                'cooling_degree_days': day_data['degreeDaySummary']['cooling']['value']
            })
        except KeyError:
            processed_data.append({
                'location_name': location_name,
                'timestamp': datetime.strptime(day_data['date'], '%Y-%m-%dT%H:%M:%S%z'),
                'temperature_min': day_data['temperature']['minimum'].get('value', -1),
                'temperature_max': day_data['temperature']['maximum'].get('value', -1),
                'temperature_avg': day_data['temperature']['average'].get('value', -1),
                'precipitation': day_data['precipitation'].get('value', -1),
                'snowfall': day_data.get('snowfall', {}).get('value', -1),
                'snow_depth': day_data.get('snowDepth', {}).get('value', -1),
                'heating_degree_days': day_data['degreeDaySummary'].get('heating', {}).get('value', -1),
                'cooling_degree_days': day_data['degreeDaySummary'].get('cooling', {}).get('value', -1)
            })
    df = pd.DataFrame(processed_data)
    return df

def get_real_time_weather(lat, lon, location_name):
    if lat and lon:
        end_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        start_date = end_date
        raw_data = fetch_weather_data(lat, lon, start_date, end_date)
        if raw_data:
            weather_df = preprocess_data(raw_data, location_name)
            return weather_df
    return pd.DataFrame()

def get_advice(cluster):
    advice = {
        0: "Prepare for a wet day with moderate temperatures. Don't forget your umbrella!", 
        1: "Expect moderate temperatures with little rain. A light jacket would be advisable.",
        2: "Expect a hot day with minimal or no rain",
        3: "It's going to be a wet and cold day. Get ready for a raincoat"
    }
    return advice.get(cluster, "No advice available for this cluster.")

def respond_to_query(query, city, weather_advice):
    doc = nlp(query)
    system_message = f"Provide advice based on current weather conditions in {city}."
    user_message = query
    assistant_message = weather_advice
    response = f"{system_message}\nUser: {user_message}\nAssistant: {assistant_message}"
    return response

def recommend_trails(temperature_avg, precipitation):
    recommended_trails = []
    for trail in trails:
        if (trail['min_temp'] <= temperature_avg <= trail['max_temp']) and (precipitation <= trail['max_precipitation']):
            recommended_trails.append(trail)
    return recommended_trails

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_query = data.get('query')
    location = data.get('location')
    lat, lon = search_address(location)
    if lat is None or lon is None:
        return jsonify({"response": "Location not found. Please try again with a different query."})
    
    real_time_data = get_real_time_weather(lat, lon, location)
    if real_time_data.empty:
        return jsonify({"response": "Could not fetch weather data. Please try again later."})

    normalized_real_time_data = scaler.transform(real_time_data[selected_columns])
    predicted_cluster = kmeans.predict(normalized_real_time_data)[0]
    weather_advice = get_advice(predicted_cluster)
    
    # Get the average temperature and precipitation from the real-time data
    temperature_avg = real_time_data['temperature_avg'].mean()
    precipitation = real_time_data['precipitation'].mean()
    
    # Recommend trails based on the weather conditions
    recommended_trails = recommend_trails(temperature_avg, precipitation)
    
    if recommended_trails:
        trails_message = "Based on the current weather conditions, here are some recommended trails:\n"
        for trail in recommended_trails:
            trails_message += f"- {trail['name']}: {trail['description']}\n"
    else:
        trails_message = "No suitable trails found based on the current weather conditions."
    
    nlp_response = respond_to_query(user_query, location, weather_advice)
    
    # Combine the weather advice and trails recommendation
    final_response = f"{nlp_response}\n\n{trails_message}"
    
    return jsonify({"response": final_response})

if __name__ == '__main__':
    # Example fitting scaler and kmeans with dummy historical data
    historical_data = pd.DataFrame({
        'temperature_min': [10, 15, 20, 25],
        'temperature_max': [20, 25, 30, 35],
        'temperature_avg': [15, 20, 25, 30],
        'precipitation': [1, 0, 2, 3],
        'snowfall': [0, 0, 0, 0],
        'snow_depth': [0, 0, 0, 0],
        'heating_degree_days': [5, 3, 1, 0],
        'cooling_degree_days': [0, 1, 3, 5]
    })
    scaler.fit(historical_data[selected_columns])
    kmeans.fit(scaler.transform(historical_data[selected_columns]))

    app.run(debug=True)
