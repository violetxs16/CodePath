#Problem 5: NFT Tag Search
#Some NFTs are grouped into collections, and each collection might contain multiple NFTs. 
# Additionally, each NFT can have a list of tags describing its style or theme 
# (e.g., "abstract", "landscape", "modern"). You need to search through these nested 
# collections to find all NFTs that contain a specific tag.

#Write the search_nft_by_tag() function, which takes in a nested list of NFT collections 
# and a tag to search for. The function should return a list of NFT names that have the specified tag.

#Evaluate the time and space complexity of your solution. Define your variables and 
# provide a rationale for why you believe your solution has the stated time and space complexity.

#Inner list will be 2

def search_nft_by_tag(nft_collections, tag):
    lst = []
    for nft in nft_collections:
        for item in nft:
            if item["tags"][0] == tag or item["tags"][1] == tag:
                lst.append(item["name"])
    #Time complexity(O(N^2))
    #Space Complexity(O(N)
    return lst

#Example Usage:

nft_collections = [
    [
        {"name": "Abstract Horizon", "tags": ["abstract", "modern"]},
        {"name": "Pixel Dreams", "tags": ["pixel", "retro"]}
    ],
    [
        {"name": "Urban Jungle", "tags": ["urban", "landscape"]},
        {"name": "City Lights", "tags": ["modern", "landscape"]}
    ]
]

nft_collections_2 = [
    [
        {"name": "Golden Hour", "tags": ["sunset", "landscape"]},
        {"name": "Sunset Serenade", "tags": ["sunset", "serene"]}
    ],
    [
        {"name": "Pixel Odyssey", "tags": ["pixel", "adventure"]}
    ]
]

nft_collections_3 = [
    [
        {"name": "The Last Piece", "tags": ["finale", "abstract"]}
    ],
    [
        {"name": "Ocean Waves", "tags": ["seascape", "calm"]},
        {"name": "Mountain Peak", "tags": ["landscape", "adventure"]}
    ]
]

print(search_nft_by_tag(nft_collections, "landscape"))
print(search_nft_by_tag(nft_collections_2, "sunset"))
print(search_nft_by_tag(nft_collections_3, "modern"))