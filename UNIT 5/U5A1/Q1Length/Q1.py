#print a question so the user knows what to enter
print("Please input a word and this program will tell you the length of the word.")

#input and set answer to a variable
word = input()

#put variable in len() and set to another variable for the value
length = len(word)

#print variable or length of the word
print(("Your word is ") + str(length)+(" characters long."))