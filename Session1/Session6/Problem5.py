#Problem 5: Merge Performance Schedules
#You are organizing a cultural festival and have two performance schedules, schedule1 and 
# schedule2, each represented by a string where each character corresponds to a performance slot. 
# Merge the schedules by adding performances in alternating order, starting with schedule1. 
# If one schedule is longer than the other, append the additional performances onto the end of the merged schedule.

#Return the merged performance schedule.

def merge_schedules(schedule1, schedule2):
    pointer1 = 0
    pointer2 = 0
    merged = ""
    while(pointer1 != len(schedule1) and pointer2 != len(schedule2)):
        merged += schedule1[pointer1]
        merged += schedule2[pointer2]
        pointer1 += 1
        pointer2 += 1
    
    if(pointer1 != len(schedule1)):
        merged += schedule1[pointer1:]
    elif(pointer2 != len(schedule2)):
        merged += schedule2[pointer2:]
    return merged

#Example Usage:

print(merge_schedules("abc", "pqr")) 
print(merge_schedules("ab", "pqrs")) 
print(merge_schedules("abcd", "pq")) 
#Understanding: We are grabbing one character starting from schedule 1 & appending it to merged schedule & keep going
#keep track of length of schedules & append remaining characters(of the longer schedule)
#Implementation: two pointer approach