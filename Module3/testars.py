def calculate_alarm_time(current_time, hours_to_wait):
    total_hours = current_time + hours_to_wait

    if total_hours >= 24:
        total_hours -= 24

    return total_hours
try:
    current_time = int(input("Enter the current time (in hours): "))
    
    # Get the number of hours to wait for the alarm
    hours_to_wait = int(input("Enter the number of hours to wait for the alarm: "))

    # Calculate the time when the alarm goes off
    alarm_time = calculate_alarm_time(current_time, hours_to_wait)

    # Display the result
    print(f"The alarm will go off at {alarm_time}:00 (24-hour clock).")

except ValueError:
    print("Invalid input. Please enter valid numeric values for the current time and hours to wait.")
