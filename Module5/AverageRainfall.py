def averageRainfall():
    num_years = int(input("Enter number of years to calculate average rainfall: "))
    start_year = 1
    num_months = num_years * 12
    total_rain  = 0.0
    while start_year <= num_years:
        for month in range(1,13):
            rainfall = float(input(f"enter the rainfall for the year {start_year} and month {month} in inches: " ))
            total_rain = total_rain + rainfall
        start_year = start_year+1
    avg_rain = total_rain/num_months
    print("\nResults")
    print(f"total number of months : {num_months}")
    print(f"total rainfall in inches : {total_rain}")
    print(f"average rainfall in inches : {avg_rain:.2f}")

averageRainfall()