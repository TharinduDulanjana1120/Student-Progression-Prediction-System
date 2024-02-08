
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
            
#Define Variables            
Progress_count=0
Module_trailer_count=0
Module_retriever_count=0
Exclude_count=0
End=0
End='y'
            
while End=='y':
    Pass = validator("pass")
    Defer = validator("defer")
    Fail = validator("fail")
    total = Pass + Defer + Fail
    if total != 120:            #Checking the total value
        print('Total incorrect.\n')
    elif Pass==120 :            #Checking the progress
        print('Progress\n')
        Progress_count=Progress_count+1
    elif Pass==100 and (Defer==20 or Fail==20):     #Checking progress module trailer
        print('Progress (module trailer)\n')
        Module_trailer_count=Module_trailer_count+1
    elif (Pass in range(0,81,20)) and (Defer in range(0,121,20)) and (Fail in range(0,61,20)): #Checking Module retriever
        print('Module retriever\n')
        Module_retriever_count=Module_retriever_count+1 
    elif (Pass in range(0,41,20)) and (Defer in range(0,41,20)) and (Fail in range(80,121,20)): #Checking Exclude
        print('Exclude\n')
        Exclude_count=Exclude_count+1
    End=input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:") #Asking from the user to continue or not
    End=End.lower()
    if  End == 'y':
        continue
    elif End == 'q':
        Total_outcomes=Progress_count+Module_trailer_count+Module_retriever_count+Exclude_count
        #Printing Histrogram
        print(f'''--------------------------------------------------------------
Histogram
Progress {Progress_count}  : {Progress_count*"*"}
Trailer {Module_trailer_count}   : {Module_trailer_count*"*"}
Retriever {Module_retriever_count} : {Module_retriever_count*"*"}
Excluded {Exclude_count}  : {Exclude_count*"*"}
{Total_outcomes} outcomes in total.
--------------------------------------------------------------''') 
        break
    else:
        print('Invalid Input')
        End=input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:")
        End=End.lower()
        while End!='y' or End=='q':
            if End=='q':
                Total_outcomes=Progress_count+Module_trailer_count+Module_retriever_count+Exclude_count
                #Printing Histrogram
                print(f'''--------------------------------------------------------------
        Histogram
        Progress {Progress_count}  : {Progress_count*"*"}
        Trailer {Module_trailer_count}   : {Module_trailer_count*"*"}
        Retriever {Module_retriever_count} : {Module_retriever_count*"*"}
        Excluded {Exclude_count}  : {Exclude_count*"*"}
        {Total_outcomes} outcomes in total.
        --------------------------------------------------------------''')
                break
            else:
                print('Invalid Input')
                End=input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:")
                End=End.lower()
                continue
    
