#Programme : B.Tech CSE
#Name : Gohil Hiren Ashvinbhai
#EnrollMent No. : 202103103510017

#------------------------------------------------------------------------------------

class employee:
    def get_data(self,emp_name,emp_age,emp_city):
        self.emp_name=emp_name
        self.emp_age=emp_age
        self.emp_city=emp_city
emp_obj=employee()
emp_obj.get_data(input("Enter The Name Of Employee : "),int(input("Enter The Age Of Employee : ")),input("Enter The Name Of City : "),)

class emp_derived(employee):
    def __init__():
        print("\n")
        print("-"*118)
        print("The Name Of Employee Is : ",emp_obj.emp_name)
        print("The Age Of Employee Is : ",emp_obj.emp_age)
        print("%s Is Belonging From %s City."%(emp_obj.emp_name,emp_obj.emp_city))
        print("-"*118)

emp_derived.__init__()

#------------------------------------------------------------------------------------