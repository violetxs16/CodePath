#Problem 4: Non-decreasing-array
#Given an array nums with n integers, write a function non_decreasing() that checks if nums could 
#become non-decreasing by modifying at most one element.

#We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

def non_decreasing(nums):
	start = 0
	end = len(nums) - 1
	counter = 0
	while(start < end):
		if nums[start] < nums[end]:
			counter += 1
			temp = nums[start]
			nums[start] = nums[end]
			nums[end] = temp
		else: 
			start += 1
			end -= 1
	return (not (counter > 1))
#Example Usage:

nums = [4, 2, 1]
print(non_decreasing(nums))