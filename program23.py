#Programme : B.Tech CSE
#Name : Gohil Hiren Ashvinbhai
#EnrollMent No. : 202103103510017

#------------------------------------------------------------------------------------
  
file = open(input("Please, Enter File Name With It's Extension: "), "r") 
take_Words = file.read()    
lower = take_Words.lower()  #Logic Of Make It Lower Case
splited=lower.split()       #Logic Of Make List (Split Method Gives Output As A List.)
print('''
Splited Form Of Given File = %s'''%splited)

x=len(splited)

print("\n")
print("The Total Words Is Presented In This File Is : ",x)

#------------------------------------------------------------------------------------