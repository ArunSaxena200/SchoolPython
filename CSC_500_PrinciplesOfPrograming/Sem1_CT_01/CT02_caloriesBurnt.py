age_years = float(input())
weight_pound = float(input())
heartRate_bpm = float(input())
time_mins = float(input())
calories_burnt = 0

calories_burnt = ((age_years * 0.2757) + (weight_pound * 0.03295) + (heartRate_bpm * 1.0781) - 75.4991) * time_mins / 8.368
print('Calories: {:.2f} calories'.format(calories_burnt))