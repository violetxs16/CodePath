#Pooh is eating all of his hunny jars in order of smallest to largest. 
# Given a list of integers hunny_jar_sizes, write a function delete_minimum_elements() that 
# continuously removes the minimum element until the list is empty. Return a new list of the elements of hunny_jar_sizes 
# in the order in which they were removed.

def delete_minimum_elements(hunny_jar_sizes):
	ordered = hunny_jar_sizes.copy()
	ordered.sort()
	return ordered

#Example Usage

hunny_jar_sizes = [5, 3, 2, 4, 1]
print(delete_minimum_elements(hunny_jar_sizes))
#Understand: We are getting the smallest element in the list and removing it through each iteraton & appending to new list in order of removal
#Plan: Create a new list based using copy and sort or we use quicksort or merge sort to sort the list then return 
