#this program is to collect the data of a road trip and calculate the each person's share of the cost
#This progrm will prompt the user for the number of people, number of days, and the cost of food and gas per day

#The program will output the total cost of each category, the total cost of the trip, and each person's share of the total cost
#developer Meyer, Brianna   02/26/2024
#-------------------------------------------------------

def main():
    print("Meyer, Brianna   CMSC 105 6388   02/26/2024")

    #prompt user for number of people going on trip. Assign variable people
    #validate is positive integer
    people=0
    while people<1:
        people=int(input("Enter the number of people on the trip :"))
        if people<1:
            print("Please enter a positive number")
    
    #prompt user for number of days of trip. assign variable days
    #validate is positive integer
    days=0
    while days<1:
        days=int(input("Enter the number of days the trip lasted :"))
        if days<1:
            print("Please enter a positive number")        

    #dayCount=1. while dayCount <= days, prompt user for cost of foodPerDay and gasPerDay
    #validate are positive integers
    dayCount=0
    foodCost=[]
    gasCost=[]
    while dayCount<days:
        dayCount=dayCount+1
        foodPerDay=-1
        gasPerDay=-1
        while foodPerDay<0:
            print("\nEnter the cost of food on day", dayCount, "in dollars :")
            foodPerDay=int(input())
            if foodPerDay<0:
                print("Please enter a positive number")
        while gasPerDay<0:
            print("Enter the cost of gas on day", dayCount, "in dollars :")
            gasPerDay=int(input())
            if gasPerDay<0:
                print("Please enter a positive number")
            
        
        #add imput foodPerDayt and gasPerDay into arrays foodCost and gasCost, respectively
        foodCost.append(foodPerDay)
        gasCost.append(gasPerDay)
           

    #sum foodCost, assign totFood, and display
    totFood=sum(foodCost)
    print("\nTotal cost of food for the trip is $", totFood)

    #sum gasCost, assign totGas and display
    totGas=sum(gasCost)
    print("Total cost of gas for the trip is $", totGas)

    #add totFood and totGas and assign variable totalCost, display
    totalCost=totFood+ totGas
    print("\nTotal cost for the trip is $", totalCost)

    #totalCost/ people = perPerson, display
    perPerson= round(totalCost/people,2)
    print("The cost of the trip per person is $", perPerson)

#----------------------------------------
main()
