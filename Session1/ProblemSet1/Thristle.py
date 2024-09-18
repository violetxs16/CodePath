#Problem 12: Thistle Hunt
#Pooh, Piglet, and Roo are looking for thistles to gift their friend Eeyore. 
#Write a function locate_thistles() that takes in a list of strings items and returns a list of the indices of 
#any elements with value "thistle". The indices in the resulting list should be ordered from least to greatest.

def locate_thistles(items):
	thistles = []
	for i in range(len(items)):
		if items[i] == "thistle":
			thistles.append(i)
	return thistles
#Example Usage

items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
print(locate_thistles(items))
#Input list of strings
#Output list of indices(ints)
#Approach, use a for loop to iterate through each element in items. Check if element == thistle & add index to new list if it does