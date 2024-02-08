from models import InventoryManager

start = input("> Press q to Quit <\n> Press enter to Start <")
print("Inventory Manager Booted!")
inventory_manager = InventoryManager()
while start.lower() != "q":
  item = input("Enter the item name: ")
  operation = input(f"{item}> ")

  if operation == "a":
    quantity = input("Enter the item quantity: ")
    cost = input("Enter the item cost: ")
    place = input("Enter the item aisle: ")
    inventory_manager.add_item(item, quantity, cost, place)
    inventory_manager.display()

  elif operation == "b":
    if item in inventory_manager.inventory:
      quantity = input("Enter ")
      inventory_manager.bimi_item(item, quantity)
      inventory_manager.display()
    else: 
      print("Item not in inventory")

