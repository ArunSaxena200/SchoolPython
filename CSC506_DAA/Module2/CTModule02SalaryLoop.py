def sal_loop(days):
    salary = 0.01  # 1 penny
    for day in range(1, days + 1):
        print(f"Day {day}: ${salary:.2f}")
        salary *= 2  # sal double

sal_loop(1000)
