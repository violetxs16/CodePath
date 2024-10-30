def power_of_four(n):

    if n == 0:
        return 1
    elif n < 0: #negative n
        return 1 / power_of_four(-n)
    else: #positive n
        return 4 * power_of_four(n - 1) #recursive case

#Write a recursive function that calculates the power of 4 raised to the nth power 
# to determine their training level.

print(power_of_four(2))
print(power_of_four(-2))