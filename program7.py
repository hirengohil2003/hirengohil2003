#Programme : B.Tech CSE
#Name : Gohil Hiren Ashvinbhai
#EnrollMent No. : 202103103510017

#------------------------------------------------------------------------------------

#Add Elements In A List..
lst=[]
n = int(input("How Many Numbers You Want To Perform :"))
for i in range(n) :
    h=int(input("Enter Numbers :"))
    lst.append(h)
print(lst)

#Number Counting Process..
num_count=int(input("Enter Which Number Do You Want To Check : "))
x=lst.count(num_count)
print("The User Entered Number %d Is Present %d Times In A List....."%(num_count,x))

#------------------------------------------------------------------------------------