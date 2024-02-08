
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
Progress_list=[]
Module_retriever_count=0
Module_retriever_list=[]
Module_trailer_count=0
Module_trailer_list=[]
Exclude_count=0
Exclude_list=[]
End='y'
            
while End=='y':
    Pass = validator("pass")
    Defer = validator("defer")
    Fail = validator("fail")
    total = Pass + Defer + Fail
    if total != 120:
        print('Total incorrect.\n')
    elif Pass==120 :
        print('Progress\n')
        Each_student=[Pass, Defer, Fail] 
        Progress_list.append(Each_student)
        Progress_count=Progress_count+1
    elif Pass==100 and (Defer==20 or Fail==20):
        print('Progress (module trailer)\n')
        Each_student=[Pass, Defer, Fail]
        Module_trailer_list.append(Each_student)
        Module_trailer_count=Module_trailer_count+1
    elif (Pass in range(0,81,20)) and (Defer in range(0,121,20)) and (Fail in range(0,61,20)):
        print('Module retriever\n')
        Each_student=[Pass, Defer, Fail]
        Module_retriever_list.append(Each_student) 
        Module_retriever_count=Module_retriever_count+1 
    elif (Pass in range(0,41,20)) and (Defer in range(0,41,20)) and (Fail in range(80,121,20)):
        print('Exclude\n')
        Each_student=[Pass, Defer, Fail]
        Exclude_list.append(Each_student)
        Exclude_count=Exclude_count+1
    End=input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:")
    End=End.lower()
    if  End == 'y':
        continue
    elif End == 'q':
        #Part (3) 
        print
        f=open('marks.txt','w') #Opening a text file
        #Writting the list elements to the text file
        for i in range(0,len(Progress_list)):
            f.write(f'Progress - {Progress_list[i][0]}, {Progress_list[i][1]}, {Progress_list[i][2]}\n')
        for i in range(0,len(Module_trailer_list)):
            f.write(f'Progress (module trailer) - {Module_trailer_list[i][0]}, {Module_trailer_list[i][1]}, {Module_trailer_list[i][2]}\n')
        for i in range(0,len(Module_retriever_list)):
            f.write(f'Module retriever - {Module_retriever_list[i][0]}, {Module_retriever_list[i][1]}, {Module_retriever_list[i][2]}\n')
        for i in range(0,len(Exclude_list)):
            f.write(f'Exclude - {Exclude_list[i][0]}, {Exclude_list[i][1]}, {Exclude_list[i][2]}')
        f.close()
        f=open('marks.txt','r')
        data=f.read() #Reading the data from the text file
        f.close()
        print(data) #Printing the data
        break
        
    else:
        print('Invalid Input')
        End=input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:")
        End=End.lower()
        while End!='y' or End=='q':
            if End=='q':
                #Part (3)
                print
                f=open('marks.txt','w') #Opening a text file
                #Writting the list elements to the text file
                for i in range(0,len(Progress_list)):
                    f.write(f'Progress - {Progress_list[i][0]}, {Progress_list[i][1]}, {Progress_list[i][2]}\n')
                for i in range(0,len(Module_trailer_list)):
                    f.write(f'Progress (module trailer) - {Module_trailer_list[i][0]}, {Module_trailer_list[i][1]}, {Module_trailer_list[i][2]}\n')
                for i in range(0,len(Module_retriever_list)):
                    f.write(f'Module retriever - {Module_retriever_list[i][0]}, {Module_retriever_list[i][1]}, {Module_retriever_list[i][2]}\n')
                for i in range(0,len(Exclude_list)):
                    f.write(f'Exclude - {Exclude_list[i][0]}, {Exclude_list[i][1]}, {Exclude_list[i][2]}')
                f.close()
                f=open('marks.txt','r')
                data=f.read()    #Reading the data from the text file
                f.close()
                print(data)  #Printing the data
                break
                
            else:
                print('Invalid Input')
                End=input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:")
                End=End.lower()
                continue
    
    
