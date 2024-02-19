#this program is to determine if a word is a palindrome, and search for the initials M or B
#prompt user for word
#assign word to variable word
#make word lowercase, assign wordLower

#run palindromeCheck function
#palindromeCheck function will take wordLower as parameter, assign word to variable original, use slice [::-1] to turn word reverse, and assign reversed word to variable reverse
#check if original == reverse, return true or false

#in program assign boolean return to variable palindrome

#run initial function with wordLower as parameter
#initial function will lastInitial= ('m' in wordChecking) and firstInitial= ('b' in wordChecking)
#return (lastInitial, firstInitial)

#main variable last= initial function returned lastInitial, main variable first= initial function returned firstInitial
#if statement: if true and true print both initials found, if true and false last initial found, if false and true first initial found, if false and false no initials found

#if palindrome== true print word is a palindrome, if false print word is not
#print if initials found

#developer: Meyer, Brianna      2/18/2024
#------------------------------------------------------------

def palindromeCheck(x):
    #palindromeCheck function will assign word to variable original
    original = x
    #use slice [::-1] to turn word reverse, and assign reversed word to variable reverse
    reverse= original[::-1]
    #check if original == reverse, return true or false
    if original == reverse:
        return(True)
    else:
        return(False)
#-------------------------------------------------------------

#initial function will lastInitial= ('m' in wordChecking) and firstInitial= ('b' in wordChecking)
def initial(x):
    wordChecking= x
    lastInitial= ('m' in wordChecking)
    firstInitial= ('b' in wordChecking)

    #return (lastInitial, firstInitial)
    return(lastInitial, firstInitial)
#--------------------------------------------------------------
def main():
    print("Meyer, Brianna    2/18/2024")
    #prompt user for word
    print("Please enter a word")
    #assign word to variable word
    word=input()
    #make word lowercase, assign wordLower
    wordLower= word.lower()

    #run palindromeCheck function
    #in program assign boolean return to variable palindrome
    palindrome= palindromeCheck(wordLower)

    #run initial function with wordLower as parameter
    #main variable last= initial function returned lastInitial, main variable first= initial function returned firstInitial
    last,first= initial(wordLower)

    #if statement: if true and true print both initials found, if true and false last initial found, if false and true first initial found, if false and false no initials found
    if (last,first)==(True, True):
        found= 'both my first and last initials are'
    elif (last,first)==(True, False):
        found= "my last initial is"
    elif (last,first)==(False, True):
        found= "my first initial is"
    else:
        found= "neither my first or last initial are"

    #if palindrome== true print word is a palindrome, if false print word is not
    if palindrome== True:
        result= "This word is a palindrome!"
    else:
        result= "This word is not a palindrome"

    #print if initials found
    print(result, "(And", found, "in this word)")
    
#---------------------------------------------------------------------
main()

    
