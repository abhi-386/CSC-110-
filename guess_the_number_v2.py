###
### Author : ABHISHEK AGARWAL
### Course : CS110 
### Descrition: This is a simplified version of GUESS THE NUMBER. It has less coding as compare to the previous function.
###             As this uses the while loop which makes the input of the values efiicient to a uper level.
###             AT LAST, IT S A REQUEST TO RUN THIS PROGRAM AS A EXTRA FEATURE IS ADDED IN THE GUESSING AREA.
from os import _exit as exit
input_number = input( "Enter number to be guessed between 1 and 100, inclusive:\n" ) # first input statement
while ( ( input_number.isnumeric() == False ) or ( int ( input_number ) > 100 ) or ( int ( input_number ) < 0 ) ): # to check wheather the number is appopre[iate or not.
    flag = 0 # counter variable to make sure the input number is integer.
    if ( input_number.isnumeric() == False ): # checking for a character
        print( input_number , "is not an acceptable value." )
        flag = 1 # it means the input string has character in it
    if ( flag != 1): # if executed it means the input string is numeric
        input_number = int( input_number )
        if ( input_number > 100 ):
            print( input_number , "is not 1-100, inclusive." )
        elif( input_number < 0 ):
            print( input_number , "is not an acceptable value." )
    input_number = input( "Enter number to be guessed between 1 and 100, inclusive:\n" )
i = 1 # To itrate the loop
while (i <= i ): #It will run as long we want
    guess = input("Enter guess "+str(i)+":\n")
    # the same fuction of this body as the above one
    while ( ( guess.isnumeric() == False ) or ( int ( guess ) > 100 ) or ( int ( guess ) < 0 ) ):
        flag = 0 
        if ( guess.isnumeric() == False ):
            print( guess , "is not an acceptable value." )
            flag = 1
        if ( flag != 1):
            guess = int( guess )
            if ( guess > 100 ):
                print( guess , "is not 1-100, inclusive." )
            elif( guess < 0 ):
                print( guess , "is not an acceptable value." )
        guess = input( "Enter guess "+str(i)+":\n" )
    if guess == input_number : # when guess number is the input number
        print(guess,"is correct! Ending game.")
        print("You used "+str(i)+" guesses to get the correct solution.")
        print("The correct number was "+str(input_number)+".")
        exit(0)
    else:
        print(guess,"is incorrect. Guess again.")
        i += 1 # keeps count of the guesses
              


        
