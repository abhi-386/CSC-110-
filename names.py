'''This is the progran where we are intoduced to exit(0)
    When the compiler comes to exit(0) the program terminates
'''
# We need to import exit from the python program
from os import _exit as exit


first = input('Enter first name: ')
if not first.isalpha() or len(first) > 30 or not first[0].isupper():
    print('Invalid first name.')
    exit(0)
    
middle = input('Enter middle initial: ')
if not middle.isalpha() or not middle[0].isupper():
    if (middle.isspace() ):
        middle = "-"
    else:
        print('Invalid middle initial.')
        exit(0)

last = input('Enter last name: ')
if not last.isalpha() or len(last) > 30 or not last[0].isupper():
    print('Invalid last name.')
    exit(0)

#Print the name when the above critria our correct
print ("Your name is :"+first+" "+middle+" "+last)
