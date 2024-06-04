import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score
import requests,numpy as np
from io import StringIO

# Load the dataset from the URL
url = "https://gist.githubusercontent.com/dhar174/14177e1d874a33bfec565a07875b875a/raw/7aa9afaaacc71aa0e8bc60b38111c24e584c74d8/data.csv"
response = requests.get(url)
data = pd.read_csv(StringIO(response.text),names=['Age', 'Height', 'Weight', 'Gender', 'Favorite Video Game Genre'],header=None)

# Display the first few rows of the dataset
print(data.head())

# Split the data into features and target variable
X = data[['Age', 'Height', 'Weight', 'Gender']]
y = data['Favorite Video Game Genre']

# Convert categorical variables into numerical values
#X = pd.get_dummies(X)
#print('******************************\n',X.head())

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=15)

# Feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# Initialize the KNN classifier
knn = KNeighborsClassifier(n_neighbors=5)

# Train the classifier
knn.fit(X_train_scaled, y_train)

# Predict the test set results
y_pred = knn.predict(X_test_scaled)
#print(y_pred)


# Evaluate the KNN classifier
print("*********Performance Metrics*********")
print("Accuracy:", accuracy_score(y_test, y_pred))


# Generate a random test row
random_test_row = pd.DataFrame({
    'Age': [25],
    'Height': [170],
    'Weight': [70],
    'Gender': ['Male']
})

# Ensure consistent feature names with training data
random_test_row = pd.get_dummies(random_test_row).reindex(columns=X.columns, fill_value=0)

# Scale the test row
random_test_row_scaled = scaler.transform(random_test_row)

# Predict the favorite video game genre for the random test row
predicted_genre = knn.predict(random_test_row_scaled)

print("Predicted favorite video game genre:", predicted_genre[0])

