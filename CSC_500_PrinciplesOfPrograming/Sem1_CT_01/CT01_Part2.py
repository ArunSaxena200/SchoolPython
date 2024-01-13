#Input from user
num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))

#Do the calculations (multiplication and division)
multiply = round(num1*num2,2)
divide = round(num1/num2,2)

#output
print("Multiplication:",num1,"*",num2,"=",multiply)
print("Division:",num1,"/",num2,"=",divide)
