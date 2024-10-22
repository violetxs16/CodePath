#Problem 8: Find Closest NFT Values 
#Buyers often look for NFTs that are closest in value to their budget. 
# Given a sorted list of NFT values and a budget, you need to find the two 
# NFT values that are closest to the given budget: one that is just below or 
# equal to the budget and one that is just above or equal to the budget. 
# If an exact match exists, it should be included as one of the values.

#Write the find_closest_nft_values() function, which takes a sorted list of 
# NFT values and a budget, and returns the pair of the two closest NFT values.

#Evaluate the time and space complexity of your solution. Define your variables 
# and provide a rationale for why you believe your solution has the stated time and space complexity.

def find_closest_nft_values(nft_values, budget):
    start = 0
    end = len(nft_values) - 1
    while(nft_values[start] <= budget):
        start += 1
    start -= 1

    while(nft_values[end] > budget):
        end -= 1
    end += 1
    return (nft_values[start], nft_values[end])
#Space complexity: O(1)
#Time complexity: 0(N)
#Example Usage:

nft_values = [3.5, 5.4, 7.2, 9.0, 10.5]
nft_values_2 = [2.0, 4.5, 6.3, 7.8, 12.1]
nft_values_3 = [1.0, 2.5, 4.0, 6.0, 9.0]

print(find_closest_nft_values(nft_values, 8.0))
print(find_closest_nft_values(nft_values_2, 6.5))
print(find_closest_nft_values(nft_values_3, 3.0))