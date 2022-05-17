# Programme : B.Tech CSE
# Name : Gohil Hiren Ashvinbhai
# EnrollMent No. : 202103103510017

# ------------------------------------------------------------------------------------

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")


while True:
    choice = int(input("Enter choice : "))

    if choice ==1:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1, "+", num2, "=", add(num1, num2))

    elif choice ==2:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice ==3:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice ==4:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1, "/", num2, "=", divide(num1, num2))

    next_Process = input("Let's do next calculation? (Y/n): ")
    if next_Process == "n":
        break

    else:
        print("Invalid Input")


# ------------------------------------------------------------------------------------
