#Problem 6: Next Greater Event
#At a cultural festival, you have a schedule of events where each event has a unique popularity score. 
# The schedule is represented by two distinct 0-indexed integer arrays schedule1 and schedule2, where 
# schedule1 is a subset of schedule2.

#For each event in schedule1, find its position in schedule2 and determine the next event in schedule2 
# with a higher popularity score. If there is no such event, then the answer for that event is -1.

#Return an array ans of length schedule1.length such that ans[i] is the next greater event's popularity 
# score as described above.

def next_greater_event(schedule1, schedule2):
    lst = []
    for item1 in schedule1:
        index1 = schedule2.index(item1)
        if(max(schedule2) > item1):#Check next event
            lst.append(max(schedule2))
        else:
            lst.append(-1)
    return lst
    




#Example Usage:

print(next_greater_event([4, 1, 2], [1, 3, 4, 2])) 
print(next_greater_event([2, 4], [1, 2, 3, 4]))
#Understand: We are given two integer arrays, output: 