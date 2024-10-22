#Problem 2: Add Furniture
#Players and villagers in Animal Crossing can add furniture to their inventory to decorate their house.

#Update the Villager class with a new method add_item() that takes in one parameter, item_name.

#The method should validate the item_name.

#If the item is valid, add item_name to the villager’s furniture attribute.
#The method does not need to return any values.
#item_name is valid if it has one of the following values: "acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", or "cacao tree".

class Villager:
    # ... methods from previous problems
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []
    def add_item(self, item_name):
        
        item = {"acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"} #or {} due to O(1) loookup time
        if item_name in item:
            self.furniture.append(item_name)
#Example Usage:

alice = Villager("Alice", "Koala", "guvnor")
print(alice.furniture)

alice.add_item("acoustic guitar")
print(alice.furniture)

alice.add_item("cacao tree")
print(alice.furniture)

alice.add_item("nintendo switch")
print(alice.furniture)