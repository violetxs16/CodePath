#Problem 5: Best Set
#As part of the festival, attendees cast votes for their favorite set. 
# Given a dictionary votes that maps attendees id numbers to the artist they voted for, 
# return the artist that had the most number of votes. If there is a tie, return any artist 
#with the top number of votes.

#Understanding: finding largest value in dictionaru
#Plan: use for loop to iterate over the votes. Have max value & check for bigger value in loop
def best_set(votes):
    dic = {}
    for vote in votes: #key is integer, value 
        if votes[vote] in dic:
            dic[votes[vote]] += 1
        else:
            dic[votes[vote]] = 1
    #override current max artist and current max value 
    artist = ""
    max_val = 0
    for key in dic:
        if dic[key] > max_val:
            artist = key#Overriding values
            max_val = dic[key]
    return artist

#Example Usage:

votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print(best_set(votes1))
print(best_set(votes2))