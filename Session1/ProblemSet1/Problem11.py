#Problem 11: T-I-Double Guh-ER
#Signs in the Hundred Acre Wood have been losing letters as Tigger bounces around stealing any letters he 
#needs to spell out his name. Write a function tiggerfy() that accepts a string s, and returns a new string 
#with the letters t, i, g, e, and r from it.

def tiggerfy(s):
	word = ""
	tiger = ["t","i","g","e","r"]
	for letter in s:
		if letter not in tiger:
			word += letter
	return word
#Example Usage

s = "suspicerous"
print(tiggerfy(s))