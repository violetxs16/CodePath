#Problem 3: Collecting Points at Festival Booths
#At the festival, there are various booths where visitors can collect points. 
# Each booth has a specific number of points available. Use a stack to simulate 
# the process of collecting points and return the total points collected after visiting all booths.

def collect_festival_points(points):
    stack = []
    for point in points:
        stack.append(point)
    return sum(stack)

#Example Usage:

print(collect_festival_points([5, 8, 3, 10])) 
print(collect_festival_points([2, 7, 4, 6])) 
print(collect_festival_points([1, 5, 9, 2, 8])) 
#Using stack & add all points to it then sum up the points