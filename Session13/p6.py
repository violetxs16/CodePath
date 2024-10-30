

def strongest_avenger(strengths):
    return helper(strengths,0)
def helper(strengths, max_num):
    #base case
    if not strengths:
        return max_num
    if strengths[0] > max_num:
        max_num = strengths[0]
    return helper(strengths[1:], max_num)
#Example Usage:

print(strongest_avenger([88, 92, 95, 99, 97, 100, 94]))
print(strongest_avenger([50, 75, 85, 60, 90]))