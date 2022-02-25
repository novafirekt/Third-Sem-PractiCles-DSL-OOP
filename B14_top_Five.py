

#Acceptance of Percentages of students : 

def Accept_Percentage(perc):
    numstud = int(input("Enter the number of students : "))
    if numstud >= 5:
        for i in range(numstud):
            perc.append(int(input("Enter the percentage of student {0}: ".format(i+1))))
        return perc
    else :
        print("Number Of students should be greater than or equal to 5 !")

#Display of roll numbers : 

def Display_Percentage(perc):
 for i in range(len(perc)):
   print(perc[i],"%")

# Function for Selection Sort of elements

def Selection_Sort(perc):
    for i in range(len(perc)):
        min= i
        for j in range(i + 1, len(perc)):
            if perc[min] > perc[j]:
                min= j
        perc[i], perc[min] = perc[min], perc[i]

    print("Marks of students after performing Selection Sort on the list : ")
    for i in range(len(perc)):
        print(perc[i])

    
# Function for Bubble Sort of elements

def Bubble_Sort(perc):
    n = len(perc)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if perc[j] > perc[j + 1]:
                perc[j], perc[j + 1] = perc[j + 1], perc[j]

    print("Marks of students after performing Bubble Sort on the list : ")
    for i in range(len(perc)):
        print(perc[i])



# Function for displaying top five percentages

def top_Five(perc):
    toplist = perc[::-1]
    for i in range (0,5):
        print(toplist[i])

#main

perc = []
flag = 1

while flag == 1:
        print("\n+---------------------MENU---------------------+")
        print("1. Accept Student percentage of students ")
        print("2. Display the percentage of Student ")
        print("3. Sort percentage from the list using sorting teqs ")
        print("4. Exit\n")

        ch = int(input("Enter your choice (from 1 to 5) : "))

        if ch == 1:
            Accept_Percentage(perc)

        elif ch == 2:
            Display_Percentage(perc)

        elif ch == 3:
            c=int(input("Select The sorting Teq : \n1) Selection Sort  \n2)Bubble Sort (1/2) : "))
            if c==1:
                Selection_Sort(perc)
                a=str(input("Do you want to display top five marks from the list ? (yes/no) : "))
                if a=='yes':
                    top_Five(perc)
                else :
                    print(" Thank You For using this sorting teq ! \n")
                    flag = 0
            else : 
                Bubble_Sort(perc)
                a=str(input("Do you want to display top five marks from the list ? (yes/no) : "))
                if a=='yes':
                    top_Five(perc)
                else :
                    print(" Thank You For using this sorting teq ! \n")
                    flag = 0
        elif ch == 4 :
            print("Thank You For Using This Program ! \n")

        else : 
            print("Enter a valid choice !!")
            flag = 0

#ktcode