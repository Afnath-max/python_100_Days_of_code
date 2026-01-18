from art import logo

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Cannot divide by 0"

def exponent(num1, num2):
    return num1 ** num2

def calculator(operator, num1, num2):
    if operator == "+":
        return add(num1, num2)
    elif operator == "-":
        return subtract(num1, num2)
    elif operator == "*":
        return multiply(num1, num2)
    elif operator == "/":
        return divide(num1, num2)
    elif operator == "^":
        return exponent(num1, num2)
    else:
        return "Invalid operator"

print(logo)

choice = True
while choice:
    number1 = int(input("Enter a number 1: "))
    operator = input("Enter an operator (+, -, *, /, ^): ")

    # Check for valid operator
    while operator not in ["+", "-", "*", "/", "^"]:
        print("Invalid operator. Please try again.")
        operator = input("Enter an operator (+, -, *, /, ^): ")

    number2 = int(input("Enter another number: "))

    # Perform the calculation
    result = calculator(operator, number1, number2)
    print(f"Result: {result}")

    # Ask if the user wants to continue
    choice = input("Do you want to continue? (y/n): ").lower() == "y"
