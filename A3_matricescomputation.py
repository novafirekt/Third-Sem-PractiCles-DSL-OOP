
print("Basic Matrix Operation using Python")
m1=[]
m=[]
m2=[]
res=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

print("Welcome to Group A ass 3")
print("For matrix operation we need some input from you please")
row1=int(input("Enter number of rows from first matrix: "))
col1=int(input("Enter number of columns from first matrix: "))
row2=int(input("Enter number of rows from second matrix: "))
col2=int(input("Enter number of columns from second matrix: "))

def main():
    print("1. Accept two matrices from user:")
    print("2. Show the matrices values:")
    print("3. Addition of two matrices:")
    print("4. Subtraction of two matrices:")
    print("5. Multiplication of two matrices:")
    print("6. Transpose of matrix:")
    print("7. Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        print("Please enter the values of first matrix:")
        accept(m1,row1,col1)
        print("Please enter the values of second matrix:")
        accept(m2,row2,col2)
        main()

    elif ch==2:
        print("The values of first matrix are as follows:")
        show(m1,row1,col1)
        print("The values of second matrix are as follows:")
        show(m2,row2,col2)
        main()

    elif ch==3:
        print("The addition of two matrices is as follows:")
        if((row1==row2)and(col1==col2)):
           add_mat(m1,m2,row1,col1)
           show(res,row1,col1)
        else:
            print("Sorry!Addition is not possible...")
        main()    
       
    elif ch==4:
        print("The subtraction of two matrices is as follows:")
        if((row1==row2)and(col1==col2)):
           sub_mat(m1,m2,row1,col1)
           show(res,row1,col1)
        else:
            print("Sorry!Subtraction is not possible...")
        main()

    elif ch==5:
        print("The Multiplication of two matrices is as follows:")
        if(col1==row2):
           mul_mat(m1,m2,row2,col1)
           show(res,row2,col1)
        else:
            print("Sorry!Multiplication is not possible...")
        main()

    elif ch==6:
        print("Before transpose of matrix the elements of matrix are as follows:")
        show(m1,row1,col1)
        print("After applying transpose the elements are as follows:")
        trans_mat(m1,row1,col1)
        show(res,row1,col1)
        main()

    elif ch==7:
        exit
    else:
        print("Please enter valid choice...")

def accept(m,row,col):
    for i in range(row):
        c=[]
        for j in range(col):
            no=int(input("Enter the value of matrix["+str(i)+"]["+str(j)+"]::"))
            c.append(no)
        print("---------------------------------------")
        m.append(c)

def show(m,row,col):
    for i in range(row):
        for j in range(col):
            print(m[i][j],end=" ")
        print()

def add_mat(m1,m2,row,col):
    for i in range(row):
        for j in range(col):
            res[i][j]=m1[i][j]+m2[i][j]

def sub_mat(m1,m2,row,col):
    for i in range(row):
        for j in range(col):
            res[i][j]=m1[i][j]-m2[i][j]

def mul_mat(m1,m2,row,col):
    for i in range(row):
        for j in range(col):
            for k in range(col):
                res[i][j]=res[i][j]+m1[i][k]*m2[k][j]

def trans_mat(m,row,col):
    for i in range(row):
        for j in range(col):
            res[i][j]=m[j][i]

main()



