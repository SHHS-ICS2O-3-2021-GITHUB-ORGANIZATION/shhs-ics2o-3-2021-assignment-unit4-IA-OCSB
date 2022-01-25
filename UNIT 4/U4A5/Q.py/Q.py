#import random to use it's function
import random

#print question so theuser enters 1 to begin the game
print("Would you like to begin The Guessing Game? Please enter one to begin.")

#set the answer to a variable 	 
game = int(input())


#use while and previous varible to set a loop
while game == 1:
  
  #Ask for a minimum and maximum an set them to a variable 
  print("Please enter a minimum for the Guessing Game:")
  minimum = int(input())

  print("Please enter a maximum for the Guessing Game:")
  maximum = int(input())
  
  #Ask the user to guess between the given minimum and maximum
  print(("Begin guessing for the number between:")+ str(minimum)+("-")+ str(maximum)) 
  
  #use random.randint to import random number between minimum and maximum
  answer = random.randint(minimum,maximum)
  
  #Create the minimum and maximum to be able to be the answer
  minimum = minimum - 1
  maximum = maximum + 1

  #variables for the number of trys later and to form a loop
  tries = 1
  guessing = 1
 
 #Loop so the user can guess multiple times before they get it right
  while guessing == 1:
    
    # the user's guess to the answer and then set it to a variable
    guess = int(input())
    
    # use if, elif and else statments to signify if the user imported the wrong answer, right answer below the minimum or above the maximum and then tell the user
    if guess != answer and guess >= maximum:
      
      print("That is incorrect and above the maximum number.")
      
      #with ever time the user gets the answer wrong they get a plus on try
      tries = tries + 1

    elif guess != answer and guess <= minimum:

      print("That is incorrect and below the minimum number.")
      
      #with ever time the user gets the answer wrong they get a plus on try
      tries = tries + 1


    elif guess != answer:

      print("Incorrect, try again...")

      #with ever time the user gets the answer wrong they get a plus on try  
      tries = tries + 1
    

    else:
      #print that the user got it right and ask them if they would like to restart
      print("Correct, would you like to restart. Please enter one to restart or any other number to quit...")

      #turn tries into a str so it can be printed with other strings
      tries = str(tries)
    
      #print the number of tries it took for the user to get it right
      print(("It took you ")+(tries)+(" tries."))


      #reset the loops
      guessing = guessing - 1

      game = game - 1 
      
      #have an input so if the user enter 1 the loop restarts and if they don't enter 1 then the loop finishes
      game = int(input())

#end once the user is done playing
print("Okay, well have a nice day. :D")