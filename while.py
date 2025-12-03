# name = input("Enter your name: ")

# while name == "":
# print("You did not enter your name")


# print(f"Hello {name}")

# age = int(input("Enter your age: "))

# while age < 0:
#   print("Age cant be negative")
#  age = int(input("Enter your age: "))

# print(f"You are {age} years old")

# food = input("Enter a food you like (q to quit): ")

# while not food == "q":
#   print(f"You like {food}")
#  food = input("Enter another food you like (q to quit): ")

# print("bye")

num = int(input("Enter number between 1 to 10:"))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter another number between 1 to 10:"))

print(f"Your number is {num}")
