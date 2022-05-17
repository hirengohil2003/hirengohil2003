#Programme : B.Tech CSE
#Name : Gohil Hiren Ashvinbhai
#EnrollMent No. : 202103103510017

#------------------------------------------------------------------------------------

f=open("hey.txt","r")
n=int(input("Enter How Many Number Of Lines You Want :"))

for i in range(n):
    f.seek(i)

print(f.tell())
print(f.readline())
f.close()

#------------------------------------------------------------------------------------