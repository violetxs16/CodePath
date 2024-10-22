#Problem 4: Telephone
#The Villager constructor has been updated to include an additional attribute neighbor. 
# A villager's neighbor is another Villager instance and represents their closest neighbor. 
# By default, a Villager's neighbor is set to None.

#Given two Villager instances start_villager and target_villager, write a function message_received() 
# that returns True if you can pass a message from the start_villager to the target_villager through a 
# series of neighbors and False otherwise.

class Villager:
    def __init__(self, name, species, personality, catchphrase, neighbor=None):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
        self.neighbor = neighbor
    # ... methods from previous problems
	
#We are given two villager instances and need to see if we can pass a message between start villager to target villager
def message_received(start_villager, target_villager):
    curr_neighbor = start_villager #Head 
    while(curr_neighbor):
        if curr_neighbor.neighbor == target_villager:
            return True
        curr_neighbor = curr_neighbor.neighbor
    return False
    #while(next != null):
        #if neightbor is target villager:
            #return True
    #return False #Not match found
#Example Usage:

isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
isabelle.neighbor = tom_nook
tom_nook.neighbor = kk_slider

print(message_received(isabelle, kk_slider))
print(message_received(kk_slider, isabelle))