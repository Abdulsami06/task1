# Grocery Store Inventory Management

# Initialize an empty inventory
inventory = []

# Function to add a new item to the inventory
def add_item():
    name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per unit: "))
    item = {"name": name, "quantity": quantity, "price": price}
    inventory.append(item)
    print(f"{name} added to the inventory.")

# Function to update the quantity of an existing item
def update_quantity():
    name = input("Enter item name to update quantity: ")
    for item in inventory:
        if item["name"] == name:
            new_quantity = int(input(f"Enter new quantity for {name}: "))
            item["quantity"] = new_quantity
            print(f"Quantity for {name} updated to {new_quantity}.")
            return
    print(f"Item {name} not found in the inventory.")

# Function to view the current inventory
def view_inventory():
    print("Current Inventory:")
    for item in inventory:
        print(f"Name: {item['name']}, Quantity: {item['quantity']}, Price: ${item['price']}")

# Function to remove an item from the inventory
def remove_item():
    name = input("Enter item name to remove: ")
    for item in inventory:
        if item["name"] == name:
            inventory.remove(item)
            print(f"{name} removed from the inventory.")
            return
    print(f"Item {name} not found in the inventory.")

# Main program loop
while True:
    print("\nMenu:")
    print("1. Add new item to inventory")
    print("2. Update item quantity")
    print("3. View current inventory")
    print("4. Remove item from inventory")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_item()
    elif choice == "2":
        update_quantity()
    elif choice == "3":
        view_inventory()
    elif choice == "4":
        remove_item()
    elif choice == "5":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

#comments:
#This program uses a list (inventory) to store information about items, and it provides a simple menu for the user to add, update, view, or remove items from the inventory.
#The program uses functions for each operation, and a while loop allows the user to perform multiple actions in a single session.
#The program will continue running until the user chooses to quit (option 5
