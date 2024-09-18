#Problem 10: Split Haycorns
#Piglet's has collected a big pile of his favorite food, haycorns, and wants to split them evenly amongst his friends. 
#Write a function split_haycorns() to help Piglet determine the number of ways he can split his haycorns into even groups.
# split_haycorns() accepts a positive integer quantity as a parameter and returns a list of all divisors of quantity.

def split_haycorns(quantity):
	resolved = []
	for i in range(1,quantity + 1):
		if quantity % i == 0:
			resolved.append(i)
	return resolved

#Example Usage

quantity = 6
print(split_haycorns(quantity))