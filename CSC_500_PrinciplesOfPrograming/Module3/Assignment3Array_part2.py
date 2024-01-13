user_time_hours = float(input("Enter the time now (24 hr format):"))
user_wait_hours = float(input("Enter the wait time (in hours):"))

def calculate_wait_time(currentTime,waitTime):
    TotalTime = currentTime + waitTime
    return TotalTime % 24

print(f"Current Time (24 hr clock):{user_time_hours:.2f}")
print(f"Wait Time (in Hours):{user_wait_hours:.2f}")
print(f"The alarm will go off at (24 hr clock):{calculate_wait_time(user_time_hours,user_wait_hours):.2f}")