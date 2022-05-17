#Programme : B.Tech CSE
#Name : Gohil Hiren Ashvinbhai
#EnrollMent No. : 202103103510017

#------------------------------------------------------------------------------------

#Add Elements In List 
list1=[]
n = int(input("How Many Numbers You Want To Check:"))
for k in range(n):
    h=int(input("Enter a Number :"))
    list1.append(h)
print("The Entered Numbers Is:",list1)

#User Define Function To Check Min. And Max. Number.
def minmax(list1):
    large=list1[0]
    small=list1[0]
    for i in range(len(list1)):
        if(large<list1[i]):
            large=list1[i]
        if(small>list1[i]):
            small=list1[i]
    return large,small

x,y=minmax(list1) 

print("The Maximum Number Is : ",x)
print("The Minimum Number Is : ",y)

#------------------------------------------------------------------------------------