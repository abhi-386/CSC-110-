###
### AUTHOR : ABHISHEK AGARWAL
###
### DESCRIPTION: THIS PROGRAM IS A BASIC MODEL OF A MONEY MANAGEMENT OF A INDIVIDUAL.
###              IT DOES SHOW HOW MUCH ARE WE SPEND OR SAVING FROM THE AMOUNT WE LEARN.
###              IT DOES HELP US TO REALISE HOW ARE WE USING OUR MONEY.
from os import _exit as exit
print("-----------------------------")
print("----- WHERE'S THE MONEY -----")
print("-----------------------------")
annual_salary = int(input("What is your annual salary?\n"))
if ( annual_salary <= 0 ):
    print( "Must enter positive integer number." )
    exit(0)
montly_rent = int(input("How much is your monthly mortgage/rent?\n"))
if ( montly_rent <= 0 ):
    print( "Must enter positive integer number." )
    exit(0)
monthly_bills = int(input("What do you spend on bills monthly?\n"))
if ( monthly_bills <= 0 ):
    print( "Must enter positive integer number." )
    exit(0)
food_expenses = int(input("What are your weekly grocery/food expenses?\n"))
if ( food_expenses <= 0 ):
    print( "Must enter positive integer number." )
    exit(0)
travel = int(input("How much do you spend on travel annually?\n"))
if ( travel <= 0 ):
    print( "Must enter positive integer number." )
    exit(0)
tax_percentage = int(input("Tax percentage?\n"))
if (tax_percentage > 100):
    print ( "Tax must be between 0% and 100%." )
    exit(0)
if ( tax_percentage < 0 ):
    print ( "Must enter positive integer number.")
    exit(0)
print()
highest_percentage = tax_percentage # KEEPING THE HIGHSET PERCENTAGE AS TAX PERCENTAGE

# Calculating the total amount to be dispalyed ON THE SCREEN

annual_rent = ( montly_rent * 12 )
annual_bills = ( monthly_bills * 12 )
annual_food_expenses = ( food_expenses * 52 )
tax = ( annual_salary * ( tax_percentage / 100.0 ))
extra = ( annual_salary - ( annual_rent + annual_bills + annual_food_expenses + travel + tax ))

# Calculating the required percentage of the given values

montly_rent_percentage = (( annual_rent / annual_salary) * 100)
if ( montly_rent_percentage >= highest_percentage ): # CHECKING IF THE HIGHEST PERCENTAGE CHANGES OR NOT!!
    highest_percentage = montly_rent_percentage
monthly_bills_percentage = (( annual_bills / annual_salary) * 100)
if ( monthly_bills_percentage >= highest_percentage ): # CHECKING IF THE HIGHEST PERCENTAGE CHANGES OR NOT!!
    highest_percentage = monthly_bills_percentage
food_expenses_percentage = (( annual_food_expenses / annual_salary) * 100)
if ( food_expenses_percentage >= highest_percentage ): # CHECKING IF THE HIGHEST PERCENTAGE CHANGES OR NOT!!
    highest_percentage = food_expenses_percentage
travel_percentage = (( travel / annual_salary) * 100)
if ( travel_percentage >= highest_percentage ): # CHECKING IF THE HIGHEST PERCENTAGE CHANGES OR NOT!!
    highest_percentage = travel_percentage
extra_percentage = (( extra / annual_salary) * 100 )
none = extra_percentage # to check if the extra is negative or positive 
if ( extra_percentage < 0 ): # IF THE EXTRA IS NEGATIVE WE ASSIGN NONE AS 0
    none = 0
else:
    if ( extra_percentage >= highest_percentage ): # CHECKING IF THE HIGHEST PERCENTAGE CHANGES OR NOT!!
        highest_percentage = extra_percentage
        
# DISPLAYING THE TABLE FORM OF BREAK DOWN
annual_salary = str(annual_salary)
print ( "-----------------------------------------"+"-" * int(highest_percentage) )
print ( "See the financial breakdown below, based on a salary of $" + annual_salary)
print ( "-----------------------------------------"+"-" * int(highest_percentage) )
print ( "| " + "mortgage/rent | $" + format( annual_rent , '10,d' ) + " |" + format( montly_rent_percentage , '6,.1f' ) + "% | " + "#" * int(montly_rent_percentage))
print ( "| " + "        bills | $" + format( annual_bills , '10,d' ) + " |" + format( monthly_bills_percentage , '6,.1f' ) + "% | " + "#" * int(monthly_bills_percentage)) 
print ( "| " + "         food | $" + format( annual_food_expenses , '10,d' ) + " |" + format( food_expenses_percentage , '6,.1f' ) + "% | " + "#" * int(food_expenses_percentage) )
print ( "| " + "       travel | $" + format( travel , '10,d' ) + " |" + format( travel_percentage , '6,.1f' ) + "% | " + "#" * int(travel_percentage))
print ( "| " + "          tax | $" + format( tax , '10,.1f' ) + " |" + format( tax_percentage , '6,.1f' )+ "% | " + "#" * int(tax_percentage) )
print ( "| " + "        extra | $" + format( extra , '10,.1f' ) + " |" + format ( extra_percentage , '6,.1f' ) + "% | " + "#" * int(none) )
print ( "-----------------------------------------"+"-" * int(highest_percentage) )
