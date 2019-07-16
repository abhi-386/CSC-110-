###
### AUTHOR : ABHISHEK AGARWAL
###
### DESCRIPTION: This is a beginning program to generate if a number is a
###              palindrome or not
def is_palindrome_word(stri):
    '''This function we willcheck if the string is  a palindrome or not
        stri: stores our original string
        Return true if stri is a plaindrome else return false;
    '''
    i = 0
    #We only require have the length of the string to check for palindrome.
    length = (len(stri) //2 ) + 1;
    while i < length:
        #check the position in the correct order
        if stri[i] != stri[len(stri) - i- 1] :
            return False
        i+=1
    return True
def main():
    #This is the main function of the program
    
    #We input a word from the user
    i = input("Enter A word: ")

    # calls the is_palindrome_word function to find out the answer
    pa = is_palindrome_word(i)
    #Display our result
    if (pa):
        print(i +" is a palindrome")
    else:
        print(i +" is not a palindrome")
main()
