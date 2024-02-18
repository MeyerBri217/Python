#This program will determine the price quote for a house cleaning service.
#The user will be prompted to enter the number of rooms in their house. House 
#size will be assigned: a small house is <=5 rooms, medium is 6-10 rooms, and
#large is 11-15 rooms.
#If the user enters over 15 rooms they will be notified this service does not clean houses that big
#The user will be prompted to choose type of cleaning
#Types of cleaning offered, and their prices per house size are as follows:
#opA- Antique Curio Dusting: Small- $150, Med- $200, Large- $250
#opB- Crime Scene cleanup: Small- $4000, Med-$6500, Large- $7500
#opC- FDA ISO class 8 cleanroom deep-clean: Small- $12000, Med- $17000, Large-$25000
#Program will output the cost of that cleaning service for that size house

# Developer: Meyer,Brianna   Date:01/30/2024
#------------------------------------------------------------
def main():

    #name, class, date
    print("Meyer, Brianna   01/30/2024")

    #Welcome message
    print("Hello! Thank you for choosing Brianna's extraregular cleaning services")

    #Prompt user for size
    rooms= eval(input("How many rooms are in the house to be cleaned? \t"))
    if (0<= rooms <= 15):
        if (0<= rooms <= 5):
            size= 'small'
        elif (6<= rooms <=10):
            size= 'med'
        elif (11<= rooms <= 15):
            size= 'large'
          
        #Define services
        opA='Antique Curio Dusting'
        opB='Crime Scene Cleanup'
        opC='ISO 8 Deep-Cleaning'
        
        print("\nThese are the services that we offer:")
        print("\nOption A: Antique Curio Dusting- your priceless family heirlooms will be \
safe and sound in the care of our insured dusting team.")
        print("\nOption B: Crime Scene Cleanup- all that evidence the police left behind \
from the previous owner's mafia dealings will be a worry of the past.")
        print("\nOption C: ISO 8 Deep-Cleaning- The best bang for your buck! You wont find a \
better deal on FDA-complient ISO class-8-cleanroom deep-cleaning anywhere else!")

        #Prompt user for service
        type=input("\nEnter the letter A, B, or C to select your cleaning service.\t")


        #Determine price
        if (type=='A'):
            opt= opA
            if size== 'small':
                cost= 150
            elif size== 'med':
                cost= 200
            elif size== 'large':
                cost= 250
        if (type=='B'):
            opt= opB
            if size== 'small':
                cost= 4000
            elif size== 'med':
                cost= 6500
            elif size== 'large':
                cost= 7500
        if (type=='C'):
            opt= opC
            if size== 'small':
                cost= 12000
            elif size== 'med':
                cost= 17000
            elif size== 'large':
                cost= 25000


        #Print Price Quote
        print(opt," in a ",size, " house will cost $",cost)
   

    else:
        print("Sorry, we cannot service a home with that many rooms.")
main()
