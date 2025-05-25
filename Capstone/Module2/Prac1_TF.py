from random import randint
from sklearn.linear_model import LinearRegression

# Step 1: Get coefficients for the equation
print("Enter coefficients for your linear equation (between 4 and 8 variables):")
while True:
    coeff_input = input("Enter coefficients separated by spaces (e.g., 1 2 3 4): ")
    coefficients = [int(x) for x in coeff_input.strip().split()]
    if 4 <= len(coefficients) <= 8:
        break
    else:
        print("Please enter between 4 and 8 coefficients.")

num_vars = len(coefficients)

# Step 2: Generate training data
TRAIN_SET_LIMIT = 1000
TRAIN_SET_COUNT = 500

TRAIN_INPUT = []
TRAIN_OUTPUT = []

for _ in range(TRAIN_SET_COUNT):
    vars_list = [randint(0, TRAIN_SET_LIMIT) for _ in range(num_vars)]
    output = sum([coeff * val for coeff, val in zip(coefficients, vars_list)])
    TRAIN_INPUT.append(vars_list)
    TRAIN_OUTPUT.append(output)

# Step 3: Train the model
model = LinearRegression()
model.fit(X=TRAIN_INPUT, y=TRAIN_OUTPUT)

# Step 4: Get test input from user
print(f"\nEnter {num_vars} values to test the model:")
while True:
    test_input = input(f"Enter {num_vars} numbers separated by spaces: ")
    test_values = [int(x) for x in test_input.strip().split()]
    if len(test_values) == num_vars:
        break
    else:
        print(f"Please enter exactly {num_vars} values.")

# Step 5: Predict and compare
predicted = model.predict([test_values])[0]
actual = sum([coeff * val for coeff, val in zip(coefficients, test_values)])

print("\n--- Result ---")
print(f"Predicted Output: {predicted:.2f}")
print(f"Actual Output (using original equation): {actual}")
print(f"Model Coefficients: {model.coef_}")
