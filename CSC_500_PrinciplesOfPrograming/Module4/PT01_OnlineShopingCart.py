class ItemToPurchase:
    def __init__(self,item_name = None,item_price = 0.0,item_qty = 0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_qty = item_qty
    
    def print_item_cost(self):
        print(f"{self.item_name} {self.item_qty} @ {self.item_price} = ${self.item_price*self.item_qty}")

#user input 1

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
item1 = ItemToPurchase(item1_name,item1_price,item1_qty)
item2 = ItemToPurchase(item2_name,item2_price,item2_qty)

#print
print("\nTOTAL COST")
item1.print_item_cost()
item2.print_item_cost()

total_cost = (item1.item_qty * item1_price) + (item2.item_qty * item2.item_price)

print(f"\nTotal: ${total_cost}")