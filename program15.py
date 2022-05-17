#Programme : B.Tech CSE
#Name : Gohil Hiren Ashvinbhai
#EnrollMent No. : 202103103510017

#------------------------------------------------------------------------------------

class university:
    def __init__(self,name,year_of_estd,city):
        self.name=name
        self.year_of_estd=year_of_estd
        self.city=city
    
class professor(university):
    def prof(self,designation,highest_qualification,area_of_research,year_of_experience,name_of_institute):
        self.designation=designation
        self.highest_qualification=highest_qualification
        self.area_of_research=area_of_research
        self.year_of_experience=year_of_experience
        self.name_of_institute=name_of_institute
    def display(self):
        print("\n")
        print("-"*118)
        print("The Name Of The University Is :",self.name) 
        print("The Year Of Establition Is : ",self.year_of_estd) 
        print("The UNIVERSITY Is Located In %s City."%self.city) 

        print("The Designation Of Professor Is :",self.designation)
        print("The Highest Qualification Of Professor Is : ",self.highest_qualification)
        print("The Area Of Reasearch Of Professor Is : ",self.area_of_research)
        print("The Year Of Experience Of Professor Is : ",self.year_of_experience,)
        print("The Name Of Institute Is :",self.name_of_institute,)
        print("-"*118)
        print("\n")
def c1():
    a=professor(input("Enter The Name Of University : "),int(input("Enter The Year Of Establition : ")),input("Enter The City Name : "))
    a.prof(input("Enter The Designation Of Professor  :"),input(" Enter The Highest Qualification Of Professor :"),input("Enter The Area Of Reasearch Of Professor: "),int(input("Enter The Year Of Experience Of Professor :")),input("Enter The Name Of Institute :"))
    a.display() 

class lab_assistant(university):
    def l_ast(self,highest_qualification,additional_skills,year_of_joining,name_of_institute):
        self.designation = "Lab Assistant"
        self.highest_qualification=highest_qualification
        self.additional_skills=additional_skills
        self.year_of_joining=year_of_joining
        self.name_of_institute=name_of_institute
    
    def display_last(self):
        print("\n")
        print("-"*118)
        print("The Name Of The University Is :",self.name)
        print("The Year Of Establition Is : ",self.year_of_estd)
        print("The UNIVERSITY Is Located In %s City."%self.city)

        print("The Designation Of Person Is : ",self.designation)
        print("The Highest Qualification Of Lab Assistant Is : ",self.highest_qualification)
        print("The Additional Skills Of Lab Assistant Is : ",self.additional_skills)
        print("The Year Of Joining Is :",self.year_of_joining)
        print("The Name Of Institute Is : ",self.name_of_institute)
        print("-"*118)
        print("\n")
def c2(): 
 b=lab_assistant(input("Enter The Name Of University : "),int(input("Enter The Year Of Establition : ")),input("Enter The City Name : "))
 b.l_ast(input("Enter The Highest Qualification Of Lab Assistant : "),input("Enter The Additional Skills Of Lab Assistant : "),int(input("Enter The Year Of Joining :")),input("The Name Of Institute : "))
 b.display_last()

class office_assistant(university):
    def o_ast(self,highest_qualification,year_of_joining,name_of_institute):
        self.designation="Office Assistant"
        self.highest_qualification=highest_qualification
        self.year_of_joining=year_of_joining
        self.name_of_institute=name_of_institute

    def display_oast(self):
        print("\n")
        print("-"*118)
        print("The Name Of The University Is :",self.name)
        print("The Year Of Establition Is : ",self.year_of_estd)
        print("The UNIVERSITY Is Located In %s City."%self.city)
        print("The Desigantion Of Person Is : ",self.designation)

        print("The Highest Qulification Of Office Assistant Is : ",self.highest_qualification)
        print("The Year Of Joining Of Office Assistant Is : ",self.year_of_joining)
        print("The Name Of Institute Is : ",self.name_of_institute)
        print("-"*118)
        print("\n")
def c3():      
 c=office_assistant(input("Enter The Name Of University : "),int(input("Enter The Year Of Establition : ")),input("Enter The City Name : "))
 c.o_ast(input("Enter The Highest Qulification Of Office Assistant : "),int(input("Enter The Year Of Joining Of Office Assistant : ")),input("Enter The Name Of Institute : "))
 c.display_oast()

class peon(university):
    def peon(self,qualification,year_of_joining,name_of_institute):
        self.designation="Office Peon"
        self.qualification=qualification
        self.year_of_joining=year_of_joining
        self.name_of_institute=name_of_institute

    def display_peon(self):
        print("\n")
        print("-"*118)
        print("The Name Of The University Is :",self.name)
        print("The Year Of Establition Is : ",self.year_of_estd)
        print("The UNIVERSITY Is Located In %s City."%self.city)
        print("The Designation Of Person Is : ",self.designation)

        print("The Qualification Of Peon Is : ",self.qualification)
        print("The Year Of Joining Of Peon Is : ",self.year_of_joining) 
        print("The Name Of Institute Is : ",self.name_of_institute)
        print("-"*118)
        print("\n")

def c4():
    d=peon(input("Enter The Name Of University : "),int(input("Enter The Year Of Establition : ")),input("Enter The City Name : "))
    d.peon(input("Enter The Qualification Of Peon : "),int(input("Enter The Year Of Joining Of Peon : ")),input("Enter The Name Of Institute : "))
    d.display_peon()
print('''Enter 1 For Professor Details 
Enter 2 For Lab Assistant Details 
Enter 3 For Office Assistant Details 
Enter 4 For Peon Details ''')
choice=int(input("Enter Your Choice :"))
if (choice==1):
    c1()
elif(choice==2):
    c2()
elif(choice==3):
    c3()
elif(choice==4):
    c4()

#------------------------------------------------------------------------------------        


