
#Acceptance of Percentages of students : 

def Accept_Percentage(perc):
    numstud = int(input("Enter the number of students : "))
    if numstud >= 5:
        for i in range(numstud):
            perc.append(float(input("Enter the percentage of student {0}: ".format(i+1))))
        return perc
    else :
        print("Number Of students should be greater than or equal to 5 !")

#Display of roll numbers : 

def Display_Percentage(perc):
 for i in range(len(perc)):
   print(perc[i],"%")

# Function for Quick Sort of elements

def partition(perc, low, high):
  pivot = perc[high]
  i = low - 1
  for j in range(low, high):
    if perc[j] <= pivot:
      i = i + 1
      (perc[i], perc[j]) = (perc[j], perc[i])
  (perc[i + 1], perc[high]) = (perc[high], perc[i + 1])
  return i + 1

def Quick_Sort(perc, low, high):
  if low < high:
    pi = partition(perc, low, high)

    Quick_Sort(perc, low, pi - 1)

    Quick_Sort(perc, pi + 1, high)


# Function for displaying top five percentages

def top_Five(perc):
    toplist = perc[::-1]
    for i in range (0,5):
        print(toplist[i])

#main

perc = []
flag = 1

while flag ==  1 :
        print("\n+---------------------MENU---------------------+")
        print("1. Accept Student percentage of students ")
        print("2. Display the percentage of Student ")
        print("3. Sort percentage from the list using Quick_Sort ")
        print("4. Exit\n")

        ch = int(input("Enter your choice (from 1 to 5) : "))

        if ch == 1:
            Accept_Percentage(perc)

        elif ch == 2:
            Display_Percentage(perc)

        elif ch == 3:
            size = len(perc)
            Quick_Sort(perc, 0, size - 1)
            print('Sorted Array in Ascending Order:')
            print(perc)

            a=str(input("Do you want to display top five marks from the list ? (y/n) : "))
            if a=='y':
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
