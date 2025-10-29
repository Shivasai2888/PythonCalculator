# pylint: disable=C0114

"""
A simple Python calculator that performs basic arithmetic operations:
Addition, Subtraction, Multiplication, and Division.
Handles division by zero and rounds results to 3 decimal places.
"""


operator = input("enter an operator (+ - * / )")

num1 = float(input("enter the first number"))
num2 = float(input("enter the second number"))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print(round(result, 3))
    else:
        print("Division by zero is not allowed")
else:
    print(f"{operator} is not valid operator ")
