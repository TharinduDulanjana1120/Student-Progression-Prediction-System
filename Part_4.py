# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: w1998804 , IIT ID:20220195 
# Date: 18/04/2022

#Process of credit input validator
def validator(types):
    "Define function to validate inputs"
    global credit
    done = False
    while not done:
        try:
            if types == "pass":
                credit = int(input("Enter your total PASS credits: "))
            elif types == "defer":
                credit = int(input("Enter your total DEFER credits: "))
            elif types == "fail":
                credit = int(input("Enter your total FAIL credits: "))

            if credit not in range(0, 121, 20):
                print("Out of range.\n")
            else:
                done = True
                return credit
        except ValueError:
            print("Integer required\n")
            
#Define variables
entered_ids=[]
Progress_count=0
Module_trailer_count=0
Module_retriever_count=0
Exclude_count=0
All_students=[]
Alpha_dict={'Student_ID':0,'Outcome':0,'Marks':0} #Intazalise a dictionary
End='y'
Outcome=0
#Getting the Student ID from the user process           
while End=='y':
    while True:
        Student_ID = input('\nEnter your Student ID: ')
        if Student_ID in entered_ids:
            print('This Student ID has already been entered. Please enter a new one.')
        else:
            entered_ids.append(Student_ID)
            break 
    Pass = validator("pass")
    Defer = validator("defer")
    Fail = validator("fail")
    total = Pass + Defer + Fail
    if total != 120:
        print('Total incorrect.\n')
    elif Pass==120 :
        print('Progress\n')
        Outcome='Progress'
        Each_student=[Pass, Defer, Fail]
        Each_Student_Results=[Student_ID, Pass, Defer, Fail, Outcome]
        All_students.append(Each_Student_Results)
        Progress_count=Progress_count+1
    elif Pass==100 and (Defer==20 or Fail==20):
        print('Progress (module trailer)\n')
        Outcome='Progress (module trailer)'
        Each_student=[Pass, Defer, Fail]
        Each_Student_Results=[Student_ID, Pass, Defer, Fail, Outcome]
        All_students.append(Each_Student_Results)
        Module_trailer_count=Module_trailer_count+1
    elif (Pass in range(0,81,20)) and (Defer in range(0,121,20)) and (Fail in range(0,61,20)):
        print('Module retriever\n')
        Outcome='Module retriever'
        Each_student=[Pass, Defer, Fail]
        Each_Student_Results=[Student_ID, Pass, Defer, Fail, Outcome]
        All_students.append(Each_Student_Results) 
        Module_retriever_count=Module_retriever_count+1 
    elif (Pass in range(0,41,20)) and (Defer in range(0,41,20)) and (Fail in range(80,121,20)):
        print('Exclude\n')
        Outcome='Exclude'
        Each_student=[Pass, Defer, Fail]
        Each_Student_Results=[Student_ID, Pass, Defer, Fail, Outcome]
        All_students.append(Each_Student_Results)
        Exclude_count=Exclude_count+1
    End=input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:")
    End=End.lower()
    if  End == 'y':
        continue
    elif End == 'q':
        
        #Part (4)
        print
        for Each_Student_Results in All_students:
            Alpha_dict['Student_ID'] = Each_Student_Results[0]
            Alpha_dict['Outcome'] = Each_Student_Results[4]
            Alpha_dict['Marks'] =Each_Student_Results[1:4]
            print(f"{Alpha_dict['Student_ID']} : {Alpha_dict['Outcome']} - {str(Alpha_dict['Marks'])[1:-1]}",end=' ')  #Printing the saved data using a for loop
          
    else:
        print('Invalid Input')
        End=input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:")
        End=End.lower()
        while End!='y' or End=='q':
            if End=='q':
                
                #Part (4)
                print
                for Each_Student_Results in All_students:
                    Alpha_dict['Student_ID'] = Each_Student_Results[0]
                    Alpha_dict['Outcome'] = Each_Student_Results[4]
                    Alpha_dict['Marks'] =Each_Student_Results[1:4]
                    print(f"{Alpha_dict['Student_ID']} : {Alpha_dict['Outcome']} - {str(Alpha_dict['Marks'])[1:-1]}",end=' ') #Printing the saved data using a for loop
                    break
            else:
                print('Invalid Input')
                End=input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:")
                End=End.lower()
                continue
             
