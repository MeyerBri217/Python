#This program is to compute the weighted average grades for students and determine which student has the highest average.
#This program will run a for loop on a list of students, Alice, Bob, Cody, and Diane
#for each student in student, call gradeCalc function, using students' names as argument
#grade calc will calculate wtAvgGrade = discussionGrade*0.15 + quizGrade*0.35 + assignmentGrade*0.5, prompting user for grades as inputs then will return wtAvgGrade
#program will assign variable studentGrade to returned wtAvgGrade, and round to two decimal points
#display student name and weighted average
#if student grade > highGrade (initalized at 0) winner=student highGrade= studentGrade
#loop until all names completed
#print winner and highGrade
#developer Meyer, Brianna   02/12/2024
#---------------------------------------------------
def gradeCalc(name):
    #prompt user for discussionGrade, quizGrade, & assignmentGrade* as inputs
    print("Enter the discussion grade for ", name, " ")
    discussionGrade=(eval(input()))
    print("Enter the quiz grade for ", name, " ")
    quizGrade=(eval(input()))
    print("Enter the assignment grade for ", name, " ")
    assignmentGrade=(eval(input()))

    #wtAvgGrade = discussionGrade*0.15 + quizGrade*0.35 + assignmentGrade*0.5
    wtAvgGrade = discussionGrade*0.15 + quizGrade*0.35 + assignmentGrade*0.5
    return(wtAvgGrade)
#-----------------------------------------
def main():
    print("Meyer, Brianna   02/12/2024")

   
   #list of students, Alice, Bob, Cody, and Diane
    students= ["Alice", "Bob", "Cody", "Diane"]
    
    #initialize winner to null and highGrade to 0
    highGrade= 0
    winner= ""

    #for each student in students, call gradeCalc function, using students' names as argument    
    for student in students:
        #program will assign variable studentGrade to returned wtAvgGrade, and round to two decimal points
        studentGrade= round(gradeCalc(student),2)
        
        #display student name and weighted average
        print("The weighted average grade for ", student, "is", studentGrade)
        
        #if student grade > highGrade winner=student highGrade= studentGrade
        if (studentGrade> highGrade):
            highGrade= studentGrade
            winner= student
    #loop until all names completed

    #print winner and highGrade
    print(winner, "has the highest weighted average grade in class, ", highGrade)

#-----------------------------------------------
main()
    
