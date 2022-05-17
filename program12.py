#Programme : B.Tech CSE
#Name : Gohil Hiren Ashvinbhai
#EnrollMent No. : 202103103510017

#------------------------------------------------------------------------------------

class student:
    def get_data(self,std_name,std_age,std_branch,std_city):
        self.std_name=std_name
        self.std_age=std_age
        self.std_branch=std_branch
        self.std_city=std_city
    def display(self):
        print("\n")
        print("-"*118)
        print("The Name Of Student Is: ",self.std_name)
        print("The Age Of Student Is: ",self.std_age)
        print("The Branch Of Student Is : ",self.std_branch)
        print("The Student Is Lived In %s City.."%(self.std_city))
        print("-"*118)

std_obj=student()
std_obj.get_data(input("Enter The Name Of Student : "),int(input("Enter The Age Of Student : ")),input("Enter The Branch Of Student : "),input("Enter The Name Of City : "))
std_obj.display()

#------------------------------------------------------------------------------------