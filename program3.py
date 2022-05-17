#Programme : B.Tech CSE
#Name : Gohil Hiren Ashvinbhai
#EnrollMent No. : 202103103510017

tup=('Hiren','Jay','Darshil','Meet') #Creation Of Tuple.
print(tup)

#count() Method..
x=tup.count('Hiren')
print(x)

#index() Method..
y=tup.index('Meet')
print(y)

#------------------------------------------------------------------------------------

# a) Demonstrate positive and negative indexing with python Tuple.

#Positive Index..
print(tup[1])

#Negative Index..
print(tup[-1])

# b) Demonstrate slicing operations on python Tuple.
print(tup[0:3])
print(tup[:-1])
print(tup[0:])

# c) Demonstrate updation on Tuple elements in python.
change_tup=list(tup)   #Convert Tuple --> List
change_tup[3]='UTU'    #Update
tup=tuple(change_tup)  #Convert List --> Tuple

print(tup)

#------------------------------------------------------------------------------------