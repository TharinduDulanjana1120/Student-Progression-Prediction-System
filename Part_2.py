# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: w1998804 , IIT ID:20220195
# Date: 18/04/2023

#Process of credit input validator
def validator(types):
    "Define function to validate inputs"
    global credit
    done = False
    while not done:
        try:
            if types == "pass":
                credit = int(input("\nEnter your total PASS credits: "))
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
Progress_count=0
Progress_list=[] #Intzalizing a list to progress
Module_retriever_count=0
Module_retriever_list=[] #Intzalizing a list to Module retriever
Module_trailer_count=0
Module_trailer_list=[] #Intzalizing a list to Module trailer
Exclude_count=0
Exclude_list=[] #Intzalizing a list to Exclude     
End='y'
            
while End=='y':
    Pass = validator("pass")
    Defer = validator("defer")
    Fail = validator("fail")
    total = Pass + Defer + Fail  #Getting the total value
    if total != 120:
        print('Total incorrect.\n')
    elif Pass==120 :
        print('Progress\n')
        Each_student=[Pass, Defer, Fail] 
        Progress_list.append(Each_student) #Append data to Progress list
        Progress_count+=1
    elif Pass==100 and (Defer==20 or Fail==20):
        print('Progress (module trailer)\n')
        Each_student=[Pass, Defer, Fail]
        Module_trailer_list.append(Each_student) #Append data to Module Trailer list
        Module_trailer_count+=1
    elif (Pass in range(0,81,20)) and (Defer in range(0,121,20)) and (Fail in range(0,61,20)):
        print('Module retriever\n')
        Each_student=[Pass, Defer, Fail]
        Module_retriever_list.append(Each_student) #Append data to Module Retriever list
        Module_retriever_count+=1 
    elif (Pass in range(0,41,20)) and (Defer in range(0,41,20)) and (Fail in range(80,121,20)):
        print('Exclude\n')
        Each_student=[Pass, Defer, Fail]
        Exclude_list.append(Each_student) #Append data to Exclude list
        Exclude_count+=1
       
    End=input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:")
    End=End.lower()
    if  End == 'y':
        continue
            
    elif End == 'q':
        #Part (2)
        #Printing the list elements 
        print
        for i in range(0,len(Progress_list)):
            print(f'Progress - {Progress_list[i][0]}, {Progress_list[i][1]}, {Progress_list[i][2]}')
        for i in range(0,len(Module_trailer_list)):
            print(f'Progress (module trailer) - {Module_trailer_list[i][0]}, {Module_trailer_list[i][1]}, {Module_trailer_list[i][2]}')
        for i in range(0,len(Module_retriever_list)):
            print(f'Module retriever - {Module_retriever_list[i][0]}, {Module_retriever_list[i][1]}, {Module_retriever_list[i][2]}')
        for i in range(0,len(Exclude_list)):
            print(f'Exclude - {Exclude_list[i][0]}, {Exclude_list[i][1]}, {Exclude_list[i][2]}')
        break
         
    else:
        print('Invalid Input')
        End=input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:")
        End=End.lower()
        while End!='y' or End=='q':
            if End=='q':
                #Part (2)
                #Printing the list elements 
                print
                for i in range(0,len(Progress_list)):
                    print(f'Progress - {Progress_list[i][0]}, {Progress_list[i][1]}, {Progress_list[i][2]}')
                for i in range(0,len(Module_trailer_list)):
                    print(f'Progress (module trailer) - {Module_trailer_list[i][0]}, {Module_trailer_list[i][1]}, {Module_trailer_list[i][2]}')
                for i in range(0,len(Module_retriever_list)):
                    print(f'Module retriever - {Module_retriever_list[i][0]}, {Module_retriever_list[i][1]}, {Module_retriever_list[i][2]}')
                for i in range(0,len(Exclude_list)):
                    print(f'Exclude - {Exclude_list[i][0]}, {Exclude_list[i][1]}, {Exclude_list[i][2]}')
                break
            else:
                print('Invalid Input')
                End=input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:")
                End=End.lower()
                continue
            
        
            
