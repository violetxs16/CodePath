#Problem 1: Reverse Sentence
#Write a function reverse_sentence() that takes in a string sentence and returns the sentence with the order of 
# the words reversed. The sentence will contain only alphabetic characters and spaces to separate the words. 
# If there is only one word in the sentence, the function should return the original string.

def reverse_sentence(sentence):
    reversed = ""
    lst_rep = list(sentence)
    word = []
    for i in range(len(lst_rep) - 1, -1, -1):
        if lst_rep[i] == " ": #Check for white space
            word.append(lst_rep[i])
            reversed += ''.join(word) #Add word to new string
            word.clear() #Reset Word
        if lst_rep[i].isalpha():#Check if it is alphabetic character else ignore
            word.insert(0,lst_rep[i])
    reversed += ''.join(word)#Insert last word that doesnt have space following it
    return reversed

#Example Usage:

sentence = "tubby little cubby all stuffed with fluff"
print(reverse_sentence(sentence))
#Understand: We are receving a string and manipulating that string. So the last word is switched with the first word & so on. Only letters & white spaces are left behind
#Plan: 
#Covert string to array, start at end & add alphabetic characters to front of new string until we hit space or letter is non alphabetic

