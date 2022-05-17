#Programme : B.Tech CSE
#Name : Gohil Hiren Ashvinbhai
#EnrollMent No. : 202103103510017

#------------------------------------------------------------------------------------

def sum(x,y):
    a=x+y
    print("The Addition Of Two Number Is : ",a)
 
def sub(x,y):
    b=x-y
    print("The Subtraction Of Two Number Is : ",b)

def mul(x,y):
    c=x*y
    print("The Multiplication Of Two Number Is : ",c)

def div(x,y):
     if(y!=0):
         d=x/y
         print("The Division Of Two Number Is : ",d)

print('''Press 1 For Addition
Press 2 For Subtraction
Press 3 For Multiplication
Press 4 For Division
''')
choice=int(input("Enter Your Choice : "))

if choice==1 :
    sum(int(input("Enter First Number : ")),int(input("Enter Second Number : ")))
elif choice==2:
    sub(int(input("Enter First Number : ")),int(input("Enter Second Number : ")))
elif choice==3:
    mul(int(input("Enter First Number : ")),int(input("Enter Second Number : ")))
elif choice==4 :
    div(int(input("Enter First Number : ")),int(input("Enter Second Number : ")))

#------------------------------------------------------------------------------------ 
 