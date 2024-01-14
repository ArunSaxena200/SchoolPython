# Step 1: ItemToPurchase class

class ItemToPurchase:
    # Attributes
    item_name = "none"
    item_price = 0.0
    item_quantity = 0

    # Default constructor
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0

    # Method
    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}")


# Step 2: Main section

# Prompt user for two items
item1 = ItemToPurchase()
print("Item 1")
item1.item_name = input("Enter the item name: ")
item1.item_price = float(input("Enter the item price: "))
item1.item_quantity = int(input("Enter the item quantity: "))

item2 = ItemToPurchase()
print("Item 2")
item2.item_name = input("Enter the item name: ")
item2.item_price = float(input("Enter the item price: "))
item2.item_quantity = int(input("Enter the item quantity: "))

# Step 3: Add costs and output total cost
total_cost = item1.item_quantity * item1.item_price + item2.item_quantity * item2.item_price
print("TOTAL COST")
item1.print_item_cost()
item2.print_item_cost()
print(f"Total: ${total_cost}")

# Step 4: ShoppingCart class

class ShoppingCart:
    # Parameterized constructor
    def __init__(self, customer_name, current_date):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    # Methods (empty for now)

    def add_item(self, item):
        pass

    def remove_item(self, item_name):
        pass

    def modify_item(self, modified_item):
        pass

    def get_num_items_in_cart(self):
        pass

    def get_cost_of_cart(self):
        pass

    def print_total(self):
        pass

    def print_descriptions(self):
        pass

# Step 5: print_menu() function

def print_menu(shopping_cart):
    while True:
        print("MENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        choice = input("Choose an option: ")

        if choice == 'a':
            # Implement Add item to cart menu option
            pass
        elif choice == 'r':
            # Implement Remove item from cart menu option
            pass
        elif choice == 'c':
            # Implement Change item quantity menu option
            pass
        elif choice == 'i':
            # Implement Output items' descriptions menu option
            pass
        elif choice == 'o':
            # Implement Output shopping cart menu option
            pass
        elif choice == 'q':
            break
        else:
            print("Invalid choice. Please choose a valid option.")

# Step 6: Implement Output shopping cart and Output item's description menu options

# Step 7: Prompt user for customer's name and today's date

# Step 8: Implement Add item to cart menu option

# Step 9: Implement Remove item from cart menu option

# Step 10: Implement Change item quantity menu option

# Main section
customer_name = input("Enter customer's name: ")
current_date = input("Enter today's date: ")

# Create a ShoppingCart object
shopping_cart = ShoppingCart(customer_name, current_date)

# Call print_menu() to start the menu loop
print_menu(shopping_cart)
