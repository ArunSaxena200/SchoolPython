
MAX_ATTEMPTS = 3
balance = 100
pin = "1234"
attempts = 0

def authenticate():
    global attempts
    while attempts < MAX_ATTEMPTS:
        entered_pin = input("Enter your PIN: ")
        if entered_pin == pin:
            print("Authentication successful.")
            return True
        else:
            attempts += 1
            print(f"Incorrect PIN. Attempt {attempts} of {MAX_ATTEMPTS}")
    print("Card blocked due to too many incorrect attempts.")
    return False

def check_balance():
    global balance
    if balance > 0:
        print(f"Your current balance is ${balance}")
        return True
    else:
        print("Account balance is zero. Account closed.")
        return False

def withdraw():
    global balance
    amount = int(input("Enter amount to withdraw: "))
    if amount <= balance:
        balance -= amount
        print(f"${amount} dispensed. Remaining balance: ${balance}")
    else:
        print("Insufficient funds.")

def atm_workflow():
    print("Welcome to the ATM")
    input("Insert your card and press Enter...")
    if authenticate():
        while True:
            print("\nTransaction Menu:")
            print("1. Check Balance")
            print("2. Withdraw")
            print("3. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                check_balance()
            elif choice == "2":
                if check_balance():
                    withdraw()
            elif choice == "3":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid option. Try again.")

if __name__ == "__main__":
    atm_workflow()
