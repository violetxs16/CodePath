def count_suits_iterative(suits):
    dic = {}
    for suit in suits:
        if suit not in dic:
            dic[suit] = 1
        else:
            dic[suit] += 1
    counter = 0
    for key in dic:
        if dic[key] == 1:
            counter += 1
    return counter
  
global_set = set()
def count_suits_recursive(suits):
    #base case
    if not suits:
        return 0
    first = suits[0]
    if first in global_set:
        return count_suits_recursive(suits[1:])
    else:
        global_set.add(first)
        return 1 + count_suits_recursive(suits[1:])

#Example Usage:

print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III"]))