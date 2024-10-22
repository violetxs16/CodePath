#Problem 3: Group by Personality
#The Villager class has been updated below to include the new string attribute 
# personality representing the character's personality type.

#Outside of the Villager class, write a function of_personality_type(). 
# Given a list of Villager instances townies and a string personality_type as parameters, 
# return a list containing the names of all villagers in townies with personality personality_type. 
# Return the names in any order.

class Villager:
    def __init__(self, name, species, personality, catchphrase):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
    # ... methods from previous problems
	 # ... methods from previous problems
    def add_item(self, item_name):
        item = {"acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"} #or {} due to O(1) loookup time
        if item_name in item:
            self.furniture.append(item_name)


def of_personality_type(townies, personality_type):
        #townies is a list of villager instances
        #We are checking each twonie personality type & see if it matches wanted personality time
        #if it does match we are returning a list
    match = []
    for towny in townies:
        if towny.personality == personality_type:
            match.append(towny.name)
    return match
#Example Usage:

isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

print(of_personality_type([isabelle, bob, stitches], "Lazy"))
print(of_personality_type([isabelle, bob, stitches], "Cranky"))