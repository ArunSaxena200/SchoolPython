def calculate_tip(foodCharges):
    tip_percent = 18
    tip_amount = foodCharges * (tip_percent/100)
    return tip_amount

#print(calculate_tip(100.00))

def calculate_sales_tax(foodCharges):
    sales_tax_percent = 7
    sales_tax = foodCharges * (sales_tax_percent/100)
    return sales_tax

#print(calculate_sales_tax(100.00))

def calculate_total_amount(foodCharges):
    total = foodCharges + calculate_tip(foodCharges) + calculate_sales_tax(foodCharges)
    return total

food_charge = float(input("Enter the total charges : $"))
print("\nBill Details\n--------------")
print(f"Food Bill      = ${food_charge:.2f}")
print(f"Sales Tax (7%) = ${calculate_sales_tax(food_charge):.2f}")
print(f"Tip (18%)      = ${calculate_tip(food_charge):.2f}")
print(f"--------------\nTotal Amount ${calculate_total_amount(food_charge):.2f}\n")
