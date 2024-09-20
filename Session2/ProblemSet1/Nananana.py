#Problem 7: NaNaNa Batman!
#Write a function nanana_batman() that accepts an integer x and prints the string "nanana batman!" where "na" is 
# repeated x times. Do not use the * operator.
def nanana_batman(x):
    if x == 0:#Case 1
        print("batman!")
    else:
        na = ""
        for i in range(x):
            na += "na"
        na += " batman!"
        print(na)
nanana_batman(0)
#Understand -> We print na until we reach x . Then concatatenote it to batman & return the string
#Plan -> Iterate from 0 to x while adding 'na' to a string outside the for loop -> Outside of for loop if x != 0 then we add space to na then concatonate it
