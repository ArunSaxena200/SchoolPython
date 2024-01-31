def sal_recur(day, salary=0.01):
    if day > 0:
        print(f"Day {day}: ${salary:.2f}")
        sal_recur(day - 1, salary * 2)

sal_recur(23.5)
