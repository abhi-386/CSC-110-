###
### Author: Benjamin Dicken
### Description: This program takes the users first, middle, and last name as input.
###              It will tell the user which two of all combinations of the three 
###              are most similar.
###

def count_same_characters(a, b):
    i = min(len(a), len(b)) - 1
    count = 0
    while i >= 0:
        if a[i] == b[i]:
            count += 1
        i -= 1
    return count
def get_name (position):
    name = input ('Enter your' + position +'name:' )
    if not name.isalpha():
        return '?'
    return name
def dispaly (a,b,c):
    most_similar = 'first and middle'
    if b > a and b > c:
        most_similar = 'first and last'
    if c > a and c > b:
        most_similar = 'middle and last'
    print('Your', most_similar, 'names are the most similar')
def main():
    first_name = get_name("first")
    middle_name = get_name("middle")
    last_name = get_name("last")
    print('welcome to the program', first_name, middle_name, last_name)
    a = count_same_characters(first_name, middle_name)
    b = count_same_characters(first_name, last_name)
    c = count_same_characters(middle_name, last_name)
    dispaly (a,b,c)
main()
