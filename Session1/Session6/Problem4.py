#Problem 4: Festival Booth Navigation
#At the cultural festival, you are managing a treasure hunt where participants need to visit 
# booths in a specific order. The order in which they should visit the booths is defined by a series of clues. 
# However, some clues lead to dead ends, and participants must backtrack to previous booths to continue their journey.

#You are given a list of clues, where each clue is either a booth number (an integer) to visit or 
# the word "back" indicating that the participant should backtrack to the previous booth.

#Write a function to simulate the participant's journey and return the final sequence of booths visited, 
# in the order they were visited.

def booth_navigation(clues):
    stack = []
    for clue in clues:
        if clue == "back":
            if len(stack) != 0:
                stack.pop()
        else:
            stack.append(clue)
    return stack

#Example Usage:

clues = [1, 2, "back", 3, 4]
print(booth_navigation(clues)) 

clues = [5, 3, 2, "back", "back", 7]
print(booth_navigation(clues)) 

clues = [1, "back", 2, "back", "back", 3]
print(booth_navigation(clues)) 

#Understanding: We are adding a clue to the stack
#Plan: use a stack & pop each time we encounter "back"