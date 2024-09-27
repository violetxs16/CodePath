#Problem 1: Balanced Art Collection
#As the curator of an art gallery, you are organizing a new exhibition. 
# You must ensure the collection of art pieces are balanced to attract the right range of buyers. 
# A balanced collection is one where the difference between the maximum and minimum value of the 
# art pieces is exactly 1.

#Given an integer array art_pieces representing the value of each art piece, write a function 
# find_balanced_subsequence() that returns the length of the longest balanced subsequence.

#A subsequence is a sequence derived from the array by deleting some or no elements without
# changing the order of the remaining elements.

#Understanding: Find a subsequence within the array that has a maximum difference of one. 

#Plan: 

def find_balanced_subsequence(art_pieces):
    #brute force approach: using two for loops
    for i in range(len(art_pieces)):
        for j in range(len()
    #Dictionary approach?
    #Number is key, count for numver is value
    #

    slow = 0
    fast = 1
    lst = []
    while(fast < len(art_pieces)):
        #What condition?

#Example Usage:

art_pieces1 = [1,3,2,2,5,2,3,7]
art_pieces2 = [1,2,3,4]
art_pieces3 = [1,1,1,1]

print(find_balanced_subsequence(art_pieces1))
print(find_balanced_subsequence(art_pieces2))
print(find_balanced_subsequence(art_pieces3))

#5
#Example 1 Explanation:  The longest balanced subsequence is [3,2,2,2,3].
#2
#0