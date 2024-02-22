#This program will determine whether a password exactly meets the following requirements for a secure password:
#The password is between 8-16 characters
#the password contains and least one number and one letter
#the password does not include any spaces.

#this program will prompt the user for a proposed password
#the proposed password will be used as the parameter for a function to check the password length
#the proposed password will be used as the parameter for a function to check if it contains at least 1 letter and 1 number
#the proposed password will be used as the parameter for a function to ensure it does not have any spaces.

#program will display if password is valid or invalid, and why.

#Meyer, Brianna     02/20/2024

#------------------------------------------
def lengthCheck(x):
    #legnthCheck function will take main password as parameter
    check= x
    #len[password] assign variable passwordLen
    passwordLen= len(check)

    #if statement to check if 8<= passwordLen <= 16
    if 8<= passwordLen<= 16:
        #return boolean
        return(True)
    else:
        return(False)    

#------------------------------------------
def alphnumCheck(password):
    
    #variable alpha= false
    alpha=False
    
    #variable num= false
    num=False

    #for character in password, .isalpha if true set alpha=true
    for character in password:
        if character.isalpha():
            alpha=True
                   
    #for character in password, .isdigit if true set num=true
    for character in password:
        if character.isdigit():
            num=True
            
    #if alpha,num == true, true return true, otherwise return false
    if (alpha, num)==(True, True):
        return(True)
    else:
        return(False)

#------------------------------------------
def spaceCheck(password):
    #if " " in password return false, else return true
    if " " in password:
        return(False)
    else:
        return(True)    

#------------------------------------------
def main():
    print("Meyer, Brianna   02/20/2024")
    
    #promp user for password, assign variable password
    print("Passwords must be between 8-16 characters long, contain at least one letter and one digit, and may not include any spaces. Enter your new password.")
    password=input()
        
    #call lengthCheck function. assign returned value to variable length
    length=lengthCheck(password)
    
    #call alphanumCheck function assign returned value to variable alphnum
    alphnum= alphnumCheck(password)
    
    #call spaceCheck function assign returned value to variable space
    space=spaceCheck(password)
    

    #if (length, alphnum, space)= True, True, True print "password is valid."
    if (length, alphnum, space)== (True, True, True):
        print("New password is valid. Congratulations.")

    #else print "password is not valid because:"
    else:
        print("That password is not valid because")

    #if length false print length is not acceptable
        if length == False:
            print("that password is not between 8-16 characters long")

    #if alphnum false print did not contain at least one number and one letter
        if alphnum == False:
            print("that password did not contain at least one letter and at least one number")

    #if space false print the password contained a space
        if space == False:
            print("that password contained a space")
        
#-----------------------------------------------
main()



