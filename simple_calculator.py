# pylint: disable=C0114

"""
A simple Python calculator that performs basic arithmetic operations:
Addition, Subtraction, Multiplication, and Division.
Handles division by zero and rounds results to 3 decimal places.
"""

operator = input("Enter an operator (+ - * /): ")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
    print("Result:", round(result, 3))
elif operator == "-":
    result = num1 - num2
    print("Result:", round(result, 3))
elif operator == "*":
    result = num1 * num2
    print("Result:", round(result, 3))
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result:", round(result, 3))
    else:
        print("Division by zero is not allowed")
else:
    print(f"{operator} is not a valid operator")
