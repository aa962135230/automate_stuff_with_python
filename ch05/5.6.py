print("**********5.6.1**********")
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(inventory):
      print("Invebtory: ")
      item_total = 0
      for k, v in inventory.items():
            print(str(v) + ' ' + k)
            item_total += v
      
      print("Total number of items: " + str(item_total))

display_inventory(stuff)

print("**********5.6.2**********")
def add_to_inventory(inventory, added_items):

      for item_name in added_items:
            if item_name in inventory.keys():
                  inventory[item_name] += 1
            else:
                  inventory.setdefault(item_name, 1)

      return inventory

inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)

