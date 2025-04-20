class ShoppingListPrototype:
    def __init__(self):
        self.pages = [
            "Welcome Screen",
            "Home Screen",
            "New List Screen",
            "List Detail Screen",
            "Edit Item Screen",
            "Settings Screen"
        ]
        self.flow = {
            "Welcome Screen": ["Home Screen"],
            "Home Screen": ["New List Screen", "List Detail Screen", "Settings Screen"],
            "New List Screen": ["List Detail Screen", "Home Screen"],
            "List Detail Screen": ["Edit Item Screen", "Home Screen"],
            "Edit Item Screen": ["List Detail Screen"],
            "Settings Screen": ["Home Screen"]
        }

    def display_summary(self):
        print("Shopping List App Prototype Summary\n")
        print(f"Total Pages: {len(self.pages)}")
        print("Pages:")
        for page in self.pages:
            print(f"  - {page}")
        print("\nPage Navigation Flow:")
        for page, next_pages in self.flow.items():
            print(f"  {page} ➝ {', '.join(next_pages)}")

if __name__ == "__main__":
    prototype = ShoppingListPrototype()
    prototype.display_summary()
