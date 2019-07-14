###
### Author: ABHISHEK AGARWAL
### Description: This program depict a Tie-fighter,according to the width the
###              user input. The length remains the same as the middle body 
###              throughout the program.

width=int(input("Enter TIE width:")) #"width" variable stores the width of the module entered by the user.
space=(width*2)+9 #"space" variable is used to mantain a specific gap in between for the first and last three lines.
print("\n")
print("|["+ " "*space+ "]|")
print("|["+ " "*space+ "]|")
print("|["+ " "*space+ "]|")
print("|["+ " "*width+ " /=---=\\ "+ " "*width+"]|")
print("|["+ " "*width+ "/==---==\\"+ " "*width+"]|")
print("|["+ "/"*width+ "|== X ==|"+ "\\"*width+"]|") # Center of the Tie-fighter where there is a physical connection between the main body and the two wings.
print("|["+ " "*width+ "\==---==/"+ " "*width+"]|")
print("|["+ " "*width+ " \=---=/ "+ " "*width+"]|")
print("|["+ " "*space+ "]|")
print("|["+ " "*space+ "]|")
print("|["+ " "*space+ "]|")


