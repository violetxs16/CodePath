#Problem 9: Pairs
#Rabbit is very particular about his belongings and wants to own an even number of each thing he owns. 
#Write a function can_pair() that accepts a list of integers item_quantities. 
#Return True if each number in item_quantities is even. Return False otherwise.

def can_pair(item_quantities):
	for number in item_quantities:
		if number % 2 != 0:
			return False
	return True


item_quantities = []
print(can_pair(item_quantities))

#Input: List of integers
#Output: Bool
