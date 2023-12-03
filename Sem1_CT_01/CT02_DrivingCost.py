price_per_mile = 0
price_20mile   = 0
price_75mile   = 0
price_500mile  = 0

miles_per_gallons = float(input())
dollars_per_gallons = float(input())

""" 20 miles-> 1 gallon - > 3.1599$ 
    20 miles -> 3.15$
    1 mile - > 3.15/20
"""
price_per_mile = dollars_per_gallons / miles_per_gallons
price_20mile = price_per_mile * 20
price_75mile = price_per_mile * 75
price_500mile = price_per_mile * 500

print('{:.2f} {:.2f} {:.2f}'.format(price_20mile,price_75mile,price_500mile))
