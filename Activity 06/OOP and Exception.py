class Item:  # Represents an item with id, name, description, and price
    def __init__(self, item_id, name, description, price):  # Initializes an Item object
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):  # Returns a formatted string representation of the Item
        return f"ID: {self.item_id}\nName: {self.name}\nDescription: {self.description}\nPrice: \u20b1{self.price:.2f}\n"


def get_valid_integer(prompt):  # Gets an integer from the user with validation
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a non-negative integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter an integer.")


def get_valid_float(prompt):  # Gets a float from the user with validation
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a non-negative number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_valid_string(prompt):  # Gets a non-empty string from the user
    while True:
        value = input(prompt).strip()
        if value:  # Check if the string is not empty
            return value
        else:
            print("Input cannot be empty.")


def create_item(items):  # Creates a new item and adds it to the list
    print("\nCreating a new item...")
    item_id = get_valid_integer("Enter item ID: ")

    # Check if ID already exists.
    for item in items:
        if item.item_id == item_id:
            print("Error: Item ID already exists.")
            return

    name = get_valid_string("Enter item name: ")
    description = get_valid_string("Enter item description: ")
    price = get_valid_float("Enter item price: ")

    new_item = Item(item_id, name, description, price)
    items.append(new_item)
    print(f"Item '{new_item.name}' added successfully!")


def view_items(items):  # Displays all items in the list in the requested format.
    print("\nList of Items:")
    if not items:
        print("No items found.")
        return
    for item in items:
        print(item)  


def update_item(items):  # Updates an existing item in the list
    print("\nUpdating an item...")
    item_id = get_valid_integer("Enter the ID of the item to update: ")

    for item in items:
        if item.item_id == item_id:
            name = get_valid_string(f"Enter new name (current: {item.name}): ")
            description = get_valid_string(f"Enter new description (current: {item.description}): ")
            price = get_valid_float(f"Enter new price (current: \u20b1{item.price:.2f}): ")

            item.name = name
            item.description = description
            item.price = price
            print(f"Item with ID {item_id} updated successfully!")
            return

    print("Item not found.")


def delete_item(items):  # Deletes an item from the list
    print("\nDeleting an item...")
    item_id = get_valid_integer("Enter the ID of the item to delete: ")

    for i, item in enumerate(items):
        if item.item_id == item_id:
            del items[i]
            print(f"Item with ID {item_id} deleted successfully!")
            return

    print("Item not found.")


def main():  # Main Function
    items = []

    while True:
        print("\n--- Item Management Application ---")
        print("[1] Create Item")
        print("[2] View Items")
        print("[3] Update Item")
        print("[4] Delete Item")
        print("[5] Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_item(items)
        elif choice == "2":
            view_items(items)
        elif choice == "3":
            update_item(items)
        elif choice == "4":
            delete_item(items)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()