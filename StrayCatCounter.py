#This progrom is to count the number of stray cats sighted in a week
#day will initialize at 1
#numcats will initialize at 0
#while day is <= 7, user will be prompted to enter number of cats seen that day
#cats that day + numcats, and day +1, then loop will restart
#when day>7, numcats will print

#developer Meyer, Brianna  02/11/2024
#---------------------------------------------------
def main():
    print("Meyer, Brianna   02/11/2024")

    #day will initialize at 1
    #numcats will initialize at 0
    day =1
    numcats=0

    #while day is <= 7, user will be prompted to enter catsday seen that day
    while(day<=7):
        print("Enter the number of (preiouvly uncounted) stray cats sighted on day", day)

        #cats that day + numcats, and day +1, then loop will restart
        numcats= numcats+ (int(input()))
        day= day+1

    #when day>7, numcats will print
    print(numcats, "stray cats were seen this week.")

#-----------------------------------------
main()
