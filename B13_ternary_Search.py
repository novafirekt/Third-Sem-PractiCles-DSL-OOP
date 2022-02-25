
 
#Accepting roll numbers : 

def Accept_roll():
 rollnum=[]
 numstud=int(input("Enter the number of students : "))
 for i in range(numstud):
  rollnum.append(int(input("Enter the roll number of student {0} : ".format(i+1))))
 return rollnum
 
#Display of roll numbers : 

def Display_roll(rollnum):
 for i in range(len(rollnum)):
   print(rollnum[i],sep= "\n")
 
#Sorting the given roll numbers : 
 
def Sort(rollnum):
 for i in range(1,len(rollnum)):
  key=rollnum[i]
  j=i-1
  while rollnum[j]>key and j>=0:
   rollnum[j+1]=rollnum[j]
   j-=1
   rollnum[j+1]=key
 return rollnum

 
#Searching through el using Ternary_Search : 

def recTernary_search(roll,left,right,findroll):
 if (right >= left):
  mid1 = left + (right - left) // 3
  mid2 = mid1 + (right - left) // 3
  if (roll[mid1] == findroll):
   return mid1
  if (roll[mid2] == findroll):
   return mid2

  if (findroll< roll[mid1]):
   return recTernary_search(roll, left, mid1 - 1, findroll)
  elif (findroll > roll[mid2]):
   return recTernary_search(roll, mid2 + 1, right, findroll)
  else:
   return recTernary_search(roll, mid1 + 1, mid2 - 1, findroll)
 return -1
        
 


#main

unsort_Roll = []
sort_Roll = []
flag = 1

while flag == 1:
        print("\n+---------------------MENU---------------------+")
        print("1. Accept Student Roll Numbers")
        print("2. Display the Roll Numbers of Student")
        print("3. Sort Roll Numbers from the list")
        print("4. Perform Recursive Ternary Search")
        print("5. Exit\n")

        ch = int(input("Enter your choice (from 1 to 6) : "))

        if ch == 1:
             unsort_Roll = Accept_roll()

        elif ch == 2:
            Display_roll(unsort_Roll)

        elif ch == 3:
            print("Elements after performing Insertion Sort : \n")
            sort_Roll = Sort(unsort_Roll)
            Display_roll(sort_Roll)

        elif ch == 4:
            findroll = int(input("Enter the Roll Number to be searched : "))
            roll=sort_Roll
            left=0
            right=len(sort_Roll)-1
            index = recTernary_search(roll,left,right,findroll)
            if index != -1:
                 print("The Roll Number",findroll,"is found at position",index+1)
            else:
                 print("Roll Number",findroll,"not found!!")
    
        elif ch == 5:
            print("Thanks for using this program!!")
            flag=0

        else:
            print("Wrong choice!!")
            flag = 0