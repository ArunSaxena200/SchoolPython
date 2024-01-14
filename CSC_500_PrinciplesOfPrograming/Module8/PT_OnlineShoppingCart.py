#Step 1- 3

class ItemToPurchase:
    def __init__(self,item_name = None,item_description =None,item_price = 0.0,item_qty = 0):
        self.item_name = item_name
        self.item_description = item_description
        self.item_price = item_price
        self.item_qty = item_qty

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_qty} @ ${self.item_price} = ${self.item_qty * self.item_price}")
    

#Step 4

class shoppingCart:
    def __init__(self, customer_name = None, current_date='01/01/2020'):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []
    '''
    add_item()
    Adds an item to cart_items list. Has parameter ItemToPurchase. Does not return anything.
    '''
    def add_Items(self,item):
        self.cart_items.append(item)
        print(f"\nitem added to the cart")

    '''
    Remove_item()
    Removes item from cart_items list. Has a string (an item's name) parameter. Does not return anything.
    If item name cannot be found, output this mesage: Item not found in cart. Nothing removed.
    '''

    def Remove_item(self,ItemName):
        for item in self.cart_items:
            if item.item_name == ItemName:
                self.cart_items.remove(item)
                return
        print("\nItem not found in cart. Nothing removed.")

    '''
    modify_item()
    Modifies an item's description, price, and/or quantity. Has parameter ItemToPurchase. Does not return anything.
    If item can be found (by name) in cart, check if parameter has default values for description, price, and quantity.
    If not, modify item in cart.
    If item cannot be found (by name) in cart, output this message: Item not found in cart. Nothing modified.
    '''

    def Modify_item(self,ItemToPurchase):
        for items in self.cart_items:
            print(items.item_name)
            if items.item_name == ItemToPurchase.item_name:
                if not items.item_description or len(ItemToPurchase.item_description) > 0:
                    items.item_description = ItemToPurchase.item_description
                if ItemToPurchase.item_price :
                    items.item_price = ItemToPurchase.item_price
                if ItemToPurchase.item_qty and ItemToPurchase.item_qty != 0:
                    items.item_qty = ItemToPurchase.item_qty
                return
        print("\nItem not found in cart. Nothing modified.")
        return
    

            
        '''
        get_num_items_in_cart()
        Returns quantity of all items in cart. Has no parameters.
        get_cost_of_cart()
        Determines and returns the total cost of items in cart. Has no parameters.

        '''

    def get_num_items_in_cart(self):
            num_items = 0
            for items in self.cart_items:
                num_items = num_items + items.item_qty
            return num_items
        
    def get_cost_of_cart(self):
            cost_cart = 0
            for items in self.cart_items:
                cost_cart = cost_cart + items.item_qty * items.item_price
            return cost_cart
        
    '''
        print_total()
        Outputs total of objects in cart.
        If cart is empty, output this message: SHOPPING CART IS EMPTY
        print_descriptions()
        Outputs each item's description.
    '''

    def print_total(self):
        print("******************")
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
            return
        print("OUTPUT SHOPPING CART")
        print("******************")
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Number of Items:", self.get_num_items_in_cart())

        for item in self.cart_items:
            print(f"{item.item_name} {item.item_qty} @ ${item.item_price} = ${item.item_qty * item.item_price}")

        print("Total: ${:.2f}".format(self.get_cost_of_cart()))

    def print_descriptions(self):
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
            return
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")

        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")

#step 5
                
def print_menu():
            print("\nMENU")
            print("a - Add item to cart")
            print("r - Remove item from cart")
            print("c - Change item quantity")
            print("i - Output items' descriptions")
            print("o - Output shopping cart")
            print("q - Quit")



def main():

    print("Item 1")
    item1_name = str(input("Enter the item1 name:\n"))
    item1_price = float(input("Enter the item1 price:\n"))
    item1_qty = int(input("Enter the item1 quantity:\n"))


    #user input 2
    print("\nItem 2")
    item2_name = str(input("Enter the item2 name:\n"))
    item2_price = float(input("Enter the item2 price:\n"))
    item2_qty = int(input("Enter the item2 quantity:\n"))

    #create objects of ItemToPurchase
    item1 = ItemToPurchase(item1_name,"",item1_price,item1_qty)
    item2 = ItemToPurchase(item2_name,"",item2_price,item2_qty)

    #print
    print("\nTOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()

    total_cost = (item1.item_qty * item1_price) + (item2.item_qty * item2.item_price)

    print(f"\nTotal: ${total_cost}")



    customer_name = input("Enter Customer's Name: ")
    current_date = input("Enter Today's Date: ")
    cart = shoppingCart(customer_name,current_date)
    cart.add_Items(item1)
    cart.add_Items(item2)
    
    print(f"\n{cart.customer_name}'s Shopping Cart - {cart.current_date}")

    


    while True:
        print_menu()
        choice = input("Choose an option: ").lower()

        if choice == 'a':
            item_name = input("Enter the item name: ")
            item_description = input("Enter the item description: ")
            item_price = float(input("Enter the item price: "))
            item_quantity = int(input("Enter the item quantity: "))
            item = ItemToPurchase(item_name, item_description, item_price, item_quantity)
            cart.add_Items(item)

        elif choice == 'r':
            item_name = input("Enter the item name to remove: ")
            cart.Remove_item(item_name)
        
        elif choice == 'c':
            item_name = input("Enter the item name to modify: ")
            item_description = input("Enter the new item description (press enter to keep the current one): ")
            item_price = float(input("Enter the new item price (press enter to keep the current one): ") or 0)
            item_quantity = int(input("Enter the new item quantity (press enter to keep the current one): ") or 0)
            item = ItemToPurchase(item_name, item_description, item_price, item_quantity)
            cart.Modify_item(item)
        
        elif choice == 'i':
            cart.print_descriptions()
        
        elif choice == 'o':
            cart.print_total()
        
        elif choice == 'q':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()