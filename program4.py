#Programme : B.Tech CSE
#Name : Gohil Hiren Ashvinbhai
#EnrollMent No. : 202103103510017

dict={"Name":"Hiren","Age":17 ,"Branch":"B.tech CSE"}
for i,j in dict.items():
    print(i,j)

#------------------------------------------------------------------------------------

# a) Demonstrate the updation of python dictionary.

dict["Progress"]="Good" #Add One (Key,Value) Pair.
print(dict)

# b) Demonstrate the removal of elements from the python dictionary.

dict.pop("Progress") #Remove Progress From Dictionary.
print(dict)

# c) Demonstrate the use of following dictionary methods - clear(), copy(), get(),items(), keys(), popitem(), and values().

#copy() Method..
x=dict.copy()
print(x)   #It Will print Copy Of Main Dictionary.

#get() Method..
res=dict.get("Name")
print(res)

#items() Method..
y=dict.items()
print(y)  #It Will Print [(Key , Value)] Paired Tuple.

#keys() Method..
keys=dict.keys()
print(keys) #It Will Print All Keys Only.

#values() Method..
values=dict.values()
print(values) #It Will Print All Values Only.

#popitem() Method..
dict.popitem() #It Will Remove Last Elements From The Dictionary.
print(dict)

#clear() Method..
dict.clear()
print(dict) #It Will Print Blank Dictionary.

#------------------------------------------------------------------------------------

