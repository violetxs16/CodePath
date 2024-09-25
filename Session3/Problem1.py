#Problem 1: Festival Lineup
#Given two lists of strings artists and set_times of length n, write a function lineup() that maps 
# each artist to their set time.

#An artist artists[i] has set time set_times[i]. Assume i <= 0 < n and len(artists) == len(set_times).

def lineup(artists, set_times):
    dic = {}
    for i in range(len(artists)):
        dic[artists[i]] = set_times[i]
    return dic

#Example Usage:

artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

print(lineup(artists1, set_times1))
print(lineup(artists2, set_times2))

#Input list of strings
#Create empty list and combine the inputs together