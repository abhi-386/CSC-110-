###
### AUTHOR: ABHISHEK AGARWAL
### COURS: CS110
### DESCRIPTION: This is a program designed on the basis of the function.
###              It contain a main function whose codes are called first
###              then the function are called from within them.
###              This program help to display three shapes with the
###              character in it is input the user:


def upward_facing_arrow(character):
        '''
        This function helps us to display a triangle which is pointing upwards
        characer: This is the only parameter variable which is printed in the triangle
        '''
        i = 6
        z = 1
        fixed = 1
        while (i > 0): # This while loop control how many lines of the triangle are to be printed out.
                space = (i - 1)
                while ( space > 0 ): # This loop help us to print out the space that form the triangles
                        print(" ",end='')
                        space -= 1
                while ( z > 0 ): # This prints out the character that form the triangle 
                        print ( character , end ='')
                        z -= 1
                print() 
                fixed += 2
                z = fixed
                i -= 1
def downward_facing_arrow(character):
        '''
        This function helps us to display a triangle which is pointing downwarsd
        characer: This is the only parameter variable which is printed in the triangle
        '''
        i = 0
        z = 11
        fixed = 11
        while (i < 6): # This while loop control how many lines of the triangle are to be printed out.
                space = i
                while ( space >= 1 ): # This loop help us to print out the space that form the triangles
                    print(" " , end='')
                    space -= 1
                while ( z > 0 ): # This prints out the character that form the triangle 
                    print ( character , end ='')
                    z -= 1
                print()
                fixed -= 2
                z = fixed 
                i += 1
def rows(height):
        '''
        This function helps us to print the horizontal rows in the three shapes
        height: This parameter varaible us to print how many vertical lines we want.
        '''
        i = 0
        while ( height > 0 ): # This loop help us to print the lines
                print ( "|---------|")
                height -= 1
def main():
        '''
        This is the main function which is called at the first when teh program runs.
        '''
        i = 1
        while ( i == 1 ):
                shape = input ( "Enter shape to display:\n")
                shape = shape.lower()
                character = input ( "Enter arrow character:\n" )
                height = int ( input ( "Enter row-area height:\n" ) )
                if ( shape == 'hourglass' or shape == 'plumbbob' or shape == 'house' ):
                    i = 2
                else:
                    print ( "!!! Enter a different shape !!!" )
                    i = 1
        print()
        if( shape == 'hourglass' ):
                 # The following function call helps us to print the shape "hourglass"
                 rows(height) 
                 downward_facing_arrow(character)
                 upward_facing_arrow(character)
                 rows(height)
        elif (shape == 'plumbbob' ):
                 # The following function call helps us to print the shape "hourglass"
                  upward_facing_arrow(character)
                  rows(height)
                  downward_facing_arrow(character)
        else:
                  # The following function call helps us to print the shape "hourglass"
                  upward_facing_arrow(character)
                  rows(height)
main()    
