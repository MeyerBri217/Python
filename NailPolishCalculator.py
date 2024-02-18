#This program is intended to determine the number of years a user's nail polish collection
#will last
#This program will prompt the user for numBottles of polish they own and numManis they do a month

#The function maniCalc will perform the fololowing steps, using a (numBottles) and b (numManis) as
#the parameters:
#multiply the numBottles by 45 to get the totManis the user's collection can produce
#multiply the numManis by 12 to get manisPerYear usage rate
#divide totManis by ManisPer Year to get totYears a collection will last (round to 1 decimal)
#return value of totyears

#The Main function will assign the value years to the value returned by maniCalc, and will
#display the value in the phrase "Your nail polish collection will last", years, "years"

#developer Meyer, Brianna   CMSC 105 6388   02/04/2024
#-----------------------------------------
def maniCalc (a,b):
    #multiply the numBottles by 45 to get the totManis the user's collection can produce
    totManis= a*45
    #multiply the numManis by 12 to get manisPerYear usage rate
    manisPerYear= b*12
    #divide totManis by ManisPer Year to get totYears a collection will last. Round to 1 decimal
    totYears= round(totManis/ manisPerYear,1)

    #return value of totyears
    return (totYears)

#---------------------------------------
def main():
    print("Meyer, Brianna   CMSC 105 6388   02/04/2024")
    #Welcome User
    print("Hello There! \nToday I am going to help you determine how long your nail polish collection\
\nwill last")
    
    #Prompt the user for numBottles of polish they own
    numBottles= eval( input("First, enter how many bottles of nail polish you own: "))
    #Prompt user for numManis they do a month
    numManis= eval(input("\nNext, enter about how many times a month do you paint your nails?\
\n(You can round or use decimals. \nFor example, I do mine every saturday so I rounded to 4.5): "))
    
    #call maniCalc # assign years
    years = maniCalc(numBottles,numManis)
    
    #display the value in the phrase "Your nail polish collection will last", years, "years"
    print("Your nail polish collection will last", years, "years")

#--------------------------------------

main()
