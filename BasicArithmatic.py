#The purpose of this program is to act as a simple calculator for basic arithmatic
#This program will prompt the user for:
#a value assigned as firstVal,
#the second value to be assigned as secondVal
#and the desired operator: +,-,*,/ (assigned as sign)

#This program will perform the arithmatic as firstVal, operator, secondVal to compute the output answer.
#The program will display an error message if an operator other than +,-,*, or / is input for sign
#The program will display an error message if the user tries to divide by 0.
#The program will output the full expression, with the answer to the arithmetic expression: firstVal, operator, secondVal "equals " answer

#Developer: Meyer, Brianna Date: 28Jan24

#-----------------------------------
#def Main
def Main():
    
#print name, class, and date
    print("Meyer, Brianna Date: 28Jan24")
    
#Greet user
    print("Welcome to the simple calculator for basic arithmatic")
    
#prompt user for firstVal
    firstVal= eval(input("Enter your first value: "))
                    
#prompt user for secondVal
    secondVal= eval(input("Enter your second value: "))
                     
#prompt user for sign
    sign= input("Enter your operator (+, -, *, or /): ")
                     
#assign +, -, *, /, strings to operator signs, and define invalid. Perform operation firstVal, sign, secondVal to find answer
    if (sign== "+" ) :
                     answer= firstVal + secondVal
                     print( firstVal, sign, secondVal, " = ", answer)
    elif (sign== "-" ):
                     answer= firstVal - secondVal
                     print( firstVal, sign, secondVal, " = ", answer)
    elif (sign== "*" ):
                     answer= firstVal * secondVal
                     print( firstVal, sign, secondVal, " = ", answer)
    elif (sign== "/" ):
                     if (secondVal != 0):
                                           answer= firstVal / secondVal
                                           print( firstVal, sign, secondVal, " = ", answer)
                     else:
                                           print("You have terribly confused this poor, simple little calculator. Please re-run the program to try again")
                                           
    
#If invalid, display error message and prompt user to try again
    else:
                     print("You have terribly confused this poor, simple little calculator. Please re-run the program to try again")                

#Signoff message
    print("Thank you for using the simple calculator for basic arithmatic!")
#--------Execute--------------------
Main()
