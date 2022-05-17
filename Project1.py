#Programme : B.tech CSE
#Name : Gohil Hiren Ashvinbhai
#Enrollment Number : 202103103510017

#---------------------------------------------------------------------------------
from re import T
from time import time
print("-"*113)
print('''                           Hello User This Is The Program Where You Able To Check Prime Number.''')
print("-"*113)
print("\n")
t=time()
print(t)
def primeNator(num1,num2):
    lower=num1
    upper=num2

    print("Prime numbers between", lower, "and", upper, "are:")

    for num in range(lower, upper + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                    print(num)   
    texe=time()-t
    print("The Execution Time Is :",texe)
primeNator(1,int(input("Enter The Largest Number Here :")))

#---------------------------------------------------------------------------------
