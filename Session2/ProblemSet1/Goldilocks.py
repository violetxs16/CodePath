#In the extended universe of fictional bears, Goldilocks finds an enticing list of numbers in the Three Bears' house. 
# She doesn't want to take a number that's too high or too low - she wants a number that's juuust right. 
# Write a function goldilocks_approved() that takes in the list of distinct positive integers nums and returns any number 
# from the list that is neither the minimum nor the maximum value in the array, or -1 if there is no such number.

#Return the selected integer.

def goldilocks_approved(nums):
    if len(nums) == 2:
        return -1
    else:
        nums.sort()
        mid = (len(nums) - 1) // 2
        return nums[mid]
#Example Usage

nums = [2, 1, 3]
print(goldilocks_approved(nums))

#Return a int that is right in the middle between the low and high numbers in the list
#Plan: Sort list, then get middle index & return number
