#Problem 3: Identify Popular Creators
#You have been tasked with identifying the most popular NFT creators in your collection. 
# A creator is considered "popular" if they have created more than one NFT in the collection.

#Write the identify_popular_creators() function, which takes a list of NFTs and returns a 
# list of the names of popular creators.

#Evaluate the time and space complexity of your solution. Define your variables and provide 
#a rationale for why you believe your solution has the stated time and space complexity.

def identify_popular_creators(nft_collection):
    names = {}
    for nft in nft_collection:
        if nft["creator"] in names:
            names[nft["creator"]] += 1
        else:
            names[nft["creator"]] = 1
    lst = []
    for creator in names:
        if names[creator] > 1:
            lst.append(creator)
    return lst
#space complexity O(N + N) -> O(N)
#time complexity O(N)
#Example Usage:
#Understanding: Input list of dictonaries. We are looking for the most popular ntfs, 
#aka appear more than once in the dictionary
#implementation: dictionary to keep track of names & values

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7},
    {"name": "Future Galaxy", "creator": "SpaceArt", "value": 8.3}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

print(identify_popular_creators(nft_collection))
print(identify_popular_creators(nft_collection_2))
print(identify_popular_creators(nft_collection_3))