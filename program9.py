#Programme : B.Tech CSE
#Name : Gohil Hiren Ashvinbhai
#EnrollMent No. : 202103103510017

#------------------------------------------------------------------------------------

print('''
      
1. Press 1 For Addition.
2. Press 2 For Subtraction.
3. Press 3 For Multiplication.
4. Press 4 For Transpose.

''')


choice=int(input("Enter your choice: "))


def add(l1, l2):
    z=[]
    for i in range(n):
        x=[]
        for j in range(n):
            x.append(0)
        z.append(x)
    

    for i in range(len(a)):
        for j in range(len(a[0])):
            z[i][j]=a[i][j] + b[i][j]
            
    return z
    
def mul(l1, l2):
    for i in range(n):
        x=[]
        for j in range(n):
            x.append(0)
        z.append(x)
    
    for i in range(len(a)):
        for j in range(len(b)):
            for k in range(len(b)):
                z[i][j] += a[i][k]*b[k][j]
    return z
    
def sub(l1, l2):
    for i in range(n):
        x=[]
        for j in range(n):
            x.append(0)
        z.append(x)
    

    for i in range(len(a)):
        for j in range(len(a[0])):
            z[i][j]=a[i][j] - b[i][j]
            
    return z

def trans(l1, l2):
    for i in range(n):
        k=[]
        for j in range(n):
            k.append(0)
        b.append(k)
 
   
    
    for i in range(len(a)):
        for j in range(len(a)):
            if i == j:
                b[i][j] = a[i][j]
            
            elif i < j:
                b[i][j] = a[j][i]
            
            elif i > j:
                b[i][j] = a[j][i]
    return b

#Addition Of Matrix..
if choice == 1:     
    a=[]
    b=[]
    z=[]
    n=int(input("Enter order of the Matrix:"))
    for i in range(n):
        x=[]
        for j in range(n):
            x.append(int(input("Enter Elements for Matrix 1:")))
        a.append(x)
    
    print("Matrix 1: ")
    for i in range(len(a)):
        print(a[i])

    for i in range(n):
        x=[]
        for j in range(n):
            x.append(int(input("Enter Elements for Matrix 2:")))
        b.append(x)
    
    print("Matrix 2: ")
    for i in range(len(a)):
        print(b[i])


    p=add(a,b)
    print("The Sum of two Matrices is:")
    for i in range(len(p)):
        print(p[i])
        
#Subtraction Of Matrix..
elif choice == 2:    
    a=[]
    b=[]
    z=[]
    n=int(input("Enter order of the Matrix:"))
    for i in range(n):
        x=[]
        
        for j in range(n):
            x.append(int(input("Enter Elements for Matrix 1:")))
        a.append(x)
        
    print("Matrix 1: ")    
    for i in range(len(a)):
        print(a[i])

    for i in range(n):
        x=[]
        for j in range(n):
            x.append(int(input("Enter Elements for Matrix 2:")))
        b.append(x)
    
    print("Matrix 2: ")
    for i in range(len(b)):
        print(b[i])

    p=sub(a,b)
    print("The Difference of two Matricss is: ")
    for i in range(len(p)):
        print(p[i])
        
#Multiplication Of Matrix...
elif choice == 3:       
    a=[]
    b=[]
    z=[]
    n=int(input("Enter order of the Matrix:"))
    for i in range(n):
        x=[]
        for j in range(n):
            x.append(int(input("Enter Elements for Matrix 1:")))
        a.append(x)
    
    print("Matrix 1: ")
    for i in range(len(a)):
        print(a[i])

    for i in range(n):
        x=[]
        for j in range(n):
            x.append(int(input("Enter Elements for Matrix 2:")))
        b.append(x)
    
    print("Matrix 2: ")
    for i in range(len(a)):
        print(b[i])

    p=mul(a,b)
    print("The Product of two Matrices is:")
    for i in range(len(p)):
        print(p[i])

#Transpose Of Matrix..
elif choice == 4:           
    a=[]
    b=[]
    n=int(input("Enter order of the Matrix:"))
    for i in range(n):
        x=[]
        for j in range(n):
            x.append(int(input("Enter Elements for Matrix 1:")))
        a.append(x)
    
    print("YOUR MATRIX is: ")
    for i in range(len(a)):
        print(a[i])
    
    
    p=trans(a,b)
    print("Transpose of the Matrix: ")
    for i in range(len(p)):
        print(p[i])
        
else: 
    print("Enter valid Choice!!")

#------------------------------------------------------------------------------------