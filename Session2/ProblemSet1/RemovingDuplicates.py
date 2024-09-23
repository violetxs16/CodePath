#Write a function remove_dupes() that accepts a sorted array items, and 
# removes the duplicates in-place such that each element appears only once. 
# Return the length of the modified array. You may not create another array; 
# your implementation must modify the original input array items.

def remove_dupes(items):

    start = 0
    for end in range(1,len(items)):
        if items[start] == items[end]:
            del items[end]
            continue
        else:
            start += 1
    #for i in range(len(items) -1): #previous approach. Logic is wrong. Did not consider bounds
     #   foward = i + 1
      ##     print(foward)
        #    print(len(items))
         ##      del items[foward]
    return items
#Example Usage

items = ["extract of malt", "haycorns", "honey", "thistle", "thistle"]
print(remove_dupes(items))
#Understand: We are given a sorted array, we must remove duplicate items in place & return the array of unique items
#Plan: Use to pointer approach. But which technique? Have pointer at startm then another at start + 1. If start + 1 == start then we delete elements until it is not. 
#Once it is not then we move start to start + 1 and do the same for the pointer
