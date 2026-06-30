import math

def addition():
    a = float(input("Please enter first number = "))
    b = float(input("Please enter second number = "))
    print(f" Result = {a + b}")

def subtraction():
    a = float(input("Please enter first number = "))
    b = float(input("Please enter second number = "))
    print(f" Result = {a - b}")

def multiplication():
    a = float(input("Please enter first number = "))
    b = float(input("Please enter second number = "))
    print(f" Result = {a * b}")

def division():
    a = float(input("Please enter first number = "))
    b = float(input("Please enter second number = "))
    if b != 0:
        print(f" Result = {a / b}")
    else:
        print("Cannot divide by zero")

def power():
    a = float(input("Please enter first number = "))
    b = float(input("Please enter second number = "))
    print(f" Result = {math.pow(a, b)}")

def square_root():
    a = float(input("Please enter number = "))
    if a >= 0:
        print(f" Result = {math.sqrt(a)}")
    else:
        print("Cannot calculate square root of negative number!")

def percentage():
    a = float(input("Please enter first number = "))
    b = float(input("Please enter second number = "))
    if b != 0:
        print(f" Result = {(a / b) * 100} %")
    else:
        print("Error: Total cannot be zero!")

def show_menu():
    while True:
        print("=== Calculator Menu ===")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. Square Root")
        print("7. Percentage")
        print("8. Exit")
        print("===================")
        choice = input("Enter your choice (1-8): ")

        if   choice == "1": addition()
        elif choice == "2": subtraction()
        elif choice == "3": multiplication()
        elif choice == "4": division()
        elif choice == "5": power()
        elif choice == "6": square_root()
        elif choice == "7": percentage()
        elif choice == "8":
            print("Thank you for using the calculator!")
            break
        else:
            print("Invalid choice! Please try again.")

        print()

show_menu()