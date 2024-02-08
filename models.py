class InventoryManager:
  def __init__(self):
    self.inventory = {}

  def add_item(self, item_name, quantity):
    self.inventory[item_name] = quantity

  def bimi_item(self, item_name, quantity):
    if item_name in self.inventory:
      self.inventory[item_name] = quantity
    else:
      print(f"This item does not exist")

  def remove_item(self, item_name, quantity):
    if item_name in self.inventory:
      if self.inventory[item_name] >= quantity:
        self.inventory[item_name] -= quantity
      else:
        print(f"Not enough {item_name} in stock to remove {quantity}") 

  def display(self):
    print("Current Inventory: ")
    for item, quantity in self.inventory.items():
      print(f"{item}: {quantity}")   