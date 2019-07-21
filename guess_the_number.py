### 
###Author: Abhishek Agarwal
###Description: This a program that focus more on if and else statements.
###             It is generally a program that helps us to guess a number which
###             it has input from the user before. There are different cases where the
###             guessed and the input number can fail. So give this a try for sure.
from os import _exit as exit
print("Enter number to be guessed between 1 and 100, inclusive:")
input_number = input()
if (input_number.isnumeric() == False): #To check if the input number is a string or float type
    print(input_number,"is not an acceptable value.")
    exit(0) # when this is executed the the program comes to an end
input_number = int(input_number) # convert to integer type from string for further comparison 
if (input_number > 100):  # to check if the input number is greater than 100
    print(input_number,"is not 1-100, inclusive.")
    exit(0)
if (input_number < 0): # to  check if the input number is less than 0
    print(input_number,"is not an acceptable value.")
    exit(0)
if (input_number >= 1 and input_number <= 100):  # this if statement is for criteria we are working on
    print("First guess:")  
    first_guess = input() # to input the value of first guess
    if first_guess.isnumeric() == 'False': #To check if the first guess is a string or float type
        print(first_guess,"is not an acceptable value.")
        exit(0)
    first_guess = int(first_guess)
    if (input_number != first_guess): # to check if the input number is not equal to first guess
        if (first_guess > 100): # to check if the first guess is greater than 100
            print(input_number,"is not inclusive in the value")
            exit(0)
        if (input_number < 0): # to  check if the first guess is less than 0
            print(input_number,"is not an acceptable value.")
            exit(0)
        else:
            print(first_guess,"is incorrect.")
            print("Second guess:")
            second_guess = input() # to input the value of second guess
            if second_guess.isnumeric() == 'False': #To check if the second guess is a string or float type
                    print(second_guess,"is not an acceptable value.")
                    exit(0)
            second_guess = int(second_guess)
            if (input_number == second_guess): # to check if the guess is correct 
                print(second_guess,"is correct! Ending game.")
                exit(0)
            if (input_number != second_guess): # to check if the input number is not equal to Second guess
                if (second_guess > 100):
                    print(second_guess,"is not inclusive in the value")
                    exit(0)
                if (input_number < 0):
                    print(input_number,"is not an acceptable value.")
                    exit(0)
                else:  # these are the last statement where the both guesses are not equal to the input number 
                    print(second_guess,"is incorrect.")
                    print("You did not guess the number within 2 attempts.")
                    print("The target number was",input_number)
                    print("Your guesses were",first_guess,"and",second_guess)
    else:
        print(first_guess,"is correct! Ending game.")
        exit(0)
