#Problem 1: NFT Name Extractor
#You're curating a large collection of NFTs for a digital art gallery, 
# and your first task is to extract the names of these NFTs from a given 
# list of dictionaries. Each dictionary in the list represents an NFT, 
# and contains information such as the name, creator, and current value.

#Write the extract_nft_names() function, which takes in this list and 
# returns a list of all NFT names.

#Evaluate the time and space complexity of your solution. 
# Define your variables and provide a rationale for why you believe 
# your solution has the stated time and space complexity.

#understanding: input: we are given a list of dictionarys(which are technically ntfs)
#Attributes of dicionaries: name, creator and current value
#Output: list of names(string)
#
#Task:

#Review the provided code and identify the bug(s).

#Explain what the bug is and how it affects the output.

#Refactor the code to fix the bug(s) and provide the correct implementation.
def extract_nft_names(nft_collection):
    nft_names = []
    for nft in nft_collection:
        nft_names.append(nft["name"])
    return nft_names
#No bugs
#O(N) time and space complexity
# Example usage:
nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Future City", "creator": "UrbanArt", "value": 3.8}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

print(extract_nft_names(nft_collection))
print(extract_nft_names(nft_collection_2))
print(extract_nft_names(nft_collection_3))