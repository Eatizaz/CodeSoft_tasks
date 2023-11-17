def addition(num1, num2):
    print("The sum of two numbers is: ", num1 + num2)

def subtraction(num1, num2):
    print("The subtraction of two numbers is: ", num1 - num2)

def multiplication(num1, num2):
    print("The multiplication of two numbers is: ", num1 * num2)

def division(num1, num2):
    if num2 != 0:
        print("The division of two numbers is: ", num1 / num2)
    else:
        print("Cannot divide by 0")

def modulus(num1, num2):
    if num2 != 0:
       print("The modulus of two numbers is: ", num1 / num2)
    else:
       print("Cannot take modulus by 0")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Press 1 for addition")
print("Press 2 for subtraction")
print("Press 3 for multiplication")
print("Press 4 for division")
print("Press 5 for modulus")


choice = int(input("Enter your choice 1-5: "))

if choice == 1:
    addition(num1, num2)
elif choice == 2:
    subtraction(num1, num2)
elif choice == 3:
    multiplication(num1, num2)
elif choice == 4:
    division(num1, num2)
elif choice == 5:
    modulus(num1, num2)
else:
    print("Invalid option")
