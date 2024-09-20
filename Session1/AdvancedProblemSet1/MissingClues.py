#Problem 5: Missing Clues
#Christopher Robin set up a scavenger hunt for Pooh, but it's a blustery day and several hidden clues have blown away. 
# Write a function find_missing_clues() to help Christopher Robin figure out which clues he needs to remake. 
# The function accepts two integers lower and upper and a unique integer array clues. 
# All elements in clues are within the inclusive range [lower, upper].

#A clue x is considered missing if x is in the range [lower, upper] and x is not in clues.

#Return the shortest sorted list of ranges that exactly covers all the missing numbers. 
# That is, no element of clues is included in any of the ranges, and each missing number is covered by one of the ranges.

def find_missing_clues(clues, lower, upper):
    missing_clues = []
    for i in range(lower,upper):
        if i not in clues:
            missing_clues.append(i)
    return missing_clues


clues = [0, 1, 3, 50, 75]
lower = 0
upper = 99
print(find_missing_clues(clues, lower, upper))

#What we know: All elemenets in array clues are within the lower and upper bounds
#What we need to do: Go from range low to upper by increment of one
#if i is not already in array clues, we add it to the missing clues array

#we are going through each element in clues so it could be 1,3,4,6,88
#clues[0] = 1
#missingclues.append([clues[i + 1],])
