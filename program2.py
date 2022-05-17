#Programme : B.Tech CSE
#Name : Gohil Hiren Ashvinbhai
#EnrollMent No. : 202103103510017

#Creation Of List.
myList=['Hiren','Jay','Darshil']
myList1=['Hiren','Jay','Darshil']
print(myList)                       #Print List

#List Methods In Pyhton.

#append() Method..
myList.append('Mom')
print(myList)

#extned() Method..
enroll=(1,2,3,4)
myList.extend(enroll)
print(myList)

#insert() Method..
myList.insert(0,'Hello') #(IndexNo. , Element)
print(myList)

#remove() Method..
myList.remove('Hello')
print(myList)

#index() Method..
x=myList.index('Hiren')
print(x)   #It Will Return Index No. Of Hiren.

#count() Method..
y=myList.count('Mom')
print(y)   #It Will Return Count Of Mom In List.

#sort() Method..
myList1.sort()
print(myList1)

#reverse() Method..
myList.reverse()
print(myList)

#copy() Method..
a=myList.copy()
print(a)

#clear() Method..
print(myList)   #It Will Return [] (Blank List).
myList.clear()

#-----------------------------------------------------------------------------------

# a) Demonstrate positive and negative indexing with python List. #

#Positive index..
print(myList1[1])  # It Will Print Second Element Of The List.

#Negative Index..
print(myList1[-1]) #It Will Print Last Element Of The List.

# b) Demonstrate slicing operations on python List.
print(myList1[0:2])
print(myList1[0:])
print(myList1[:-1])

# c) Demonstrate updation on List elements in python.
myList1.append(['Hemant','Varsha','Sharad','Shishir'])
print(myList1)    #It Will print Updated List.

# d) Demonstrate deletion of a single python list element and multiple elements using slicing operator.
myList1.remove('Darshil') #Deletation Of Single Element. 
print(myList1)

del myList1[0:2] #Deletation Of Multiple Element. 
print(myList1)

#-----------------------------------------------------------------------------------