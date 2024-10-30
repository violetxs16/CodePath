def count_suits_iterative(suits):
    count = 0
    for item in suits:
        count += 1
    return count

def count_suits_recursive(suits):
    #base case
    if len(suits) == 0:
        return 0
    #recursive
    return 1 + count_suits_iterative(suits[1:])
#Example Usage:

print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III", "Mark IV"]))

