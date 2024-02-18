#The purpose of this program is to compute the daily pay for an Uber driver
#The user will be prompted for the number of hours driven, the number of miles driven, and the total tips received
#The total pay will be computed using the user input variables, and the known constants 0.16 (16 cents) commission per mile, and $15 pay per hour, added to the tips received.

#Developer Meyer, Brianna   Date: 01/21/2024

def main():
    #Welcome message
    print("Meyer, Brianna   01/21/2024")
    print("Your hourly rate is $15 per hour \nYour commisions is 0.16 cents per mile.")
    print("To calculate your daily total pay: \n")

    #Prompt the user for hours worked and designate as hoursworked
    hoursworked= float(input("Enter the number of hours you worked today: \t"))

    #Prompt the user for miles driven and designate as milesdriven
    milesdriven= float(input("Enter the number of miles you drove today: \t"))

    #Prompt the user for the amount of tips received and designate as tips
    tips= float(input("Enter the amount you received in tips today: \t"))

    #compute wage as hoursworked * 15 per hour
    wage=hoursworked*15

    #compute commission as milesdriven * 0.16 per mile
    commission=milesdriven*0.16

    #Calculate totalpay for the day as the sum of wage, commission, and tips
    totalpay= wage+commission+tips

    #display wage
    print("Your earned wage today is ", wage)

    #display commission
    print("Your earned commission today is ",commission)

    #display tips
    print("Your tips received today is ",tips)

    #Display total pay for the day
    print("Your total pay for the day is ", totalpay)

#----Execute-----
               
main()

