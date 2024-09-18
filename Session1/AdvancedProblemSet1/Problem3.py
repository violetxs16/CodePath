#Problem 3: T-I-Double Guh-Er II
#T-I-Double Guh-Er: That spells Tigger! Write a function tiggerfy() that accepts a string word and 
# returns a new string that removes any substrings t, i, gg, and er from word. 
# The function should be case insensitive.

def tiggerfy(word):
	
	non_tigger = word[:].lower()
	substr = ["t","i","gg","er"]
	for sub in substr:
		non_tigger = non_tigger.replace(sub,"")
	return non_tigger
			
#Example Usage:

word = "Trigger"
print(tiggerfy(word))

#Input: string
#Output: String
#Approach: Iterate through word, indexing each char. Lower char to lower case & compare agaisnt the substrings. If ot a match add to new substring

