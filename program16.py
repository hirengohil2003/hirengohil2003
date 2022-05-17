#Programme : B.Tech CSE
#Name : Gohil Hiren Ashvinbhai
#EnrollMent No. : 202103103510017

#------------------------------------------------------------------------------------

class c:
    def __init__(self, c_learning, name_professor):

        self.name_professor = name_professor
        self.c_learning = c_learning
        self.print_learning = self.c_learning.split()

class python:
    def __init__(self, py_learning, name_professor):
        self.py_learning = py_learning
        self.name_professor = name_professor
        self.print_learning = self.py_learning.split()

class web_designing:
    def __init__(self, wd_learning, name_professor):
        self.wd_learning = wd_learning
        self.name_professor = name_professor
        self.print_learning = self.wd_learning.split()

class student(c, python, web_designing):

    def __init__(self, std_name, std_enroll_no, std_course):
        self.college = "Asha M. Tarsadia Institute Of Computer Science And Technology."
        self.std_name = std_name
        self.std_enroll_no = std_enroll_no
        self.std_course = std_course

print('''Enter 1 For Check Progress In C language.
Enter 2 For Check Progress In Python language.
Enter 3 For Check Progress In Web Designing.''')

choice = int(input("Enter Choice : "))

def display_c():
    std1 = student(input("Enter Student Name :"), int(
        input("Enrollment No.")), input("Enter courese :"))
    c1 = c(input('Enter Topics of C Language Separated by Space :'),
           input("Enter The Name Of Professor : "))
    print("\n")
    print("-"*118)
    print("The Name Of College Is : ", std1.college)
    print("The Student Name Is :", std1.std_name)
    print("The Enrollment No. Of Student Is : ", std1.std_enroll_no)
    print("The Students's Course Name Is : ", std1.std_course)
    print("The Name Of Professor Is : ",c1.name_professor)
    print("The Topics Covered In C Language By Professor Is : ",c1.print_learning)
    print("-"*118)
    print("\n")
    
def display_python():
    std1 = student(input("Enter Student Name :"), int(
        input("Enrollment No.")), input("Enter courese :"))
    c2 = python(input('Enter Topics of Python Language Separated by Space :'), input(
        "Enter The Name Of Professor : "))
    print("\n")
    print("-"*118)
    print("The Name Of College Is : ", std1.college)
    print("The Student Name Is :", std1.std_name)
    print("The Enrollment No. Of Student Is : ", std1.std_enroll_no)
    print("The Students's Course Name Is : ", std1.std_course)
    print("The Name Of Professor Is : ",c2.name_professor)
    print("The Topics Covered Python Language By Professor Is : ",c2.print_learning)
    print("-"*118)
    print("\n")

def display_wd():
    std1 = student(input("Enter Student Name :"), int(
        input("Enrollment No.")), input("Enter courese :"))
    c3 = web_designing(input('Enter Topics Of Web Designing Separated by Space : '), input(
        "Enter The Name Of Professor : "))
    print("\n")
    print("-"*118)
    print("The Name Of College Is : ", std1.college)
    print("The Student Name Is :", std1.std_name)
    print("The Enrollment No. Of Student Is : ", std1.std_enroll_no)
    print("The Students's Course Name Is : ", std1.std_course)
    print("The Name Of Professor Is : ",c3.name_professor)
    print("The Topics Covered In Web Designing By Professor Is : ",c3.print_learning)
    print("-"*118)
    print("\n")


if(choice == 1):
    display_c()
elif(choice == 2):
    display_python()
elif(choice == 3):
    display_wd()

#------------------------------------------------------------------------------------

