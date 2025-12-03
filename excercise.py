username = input("Enter a username: ")


if len(username) > 14:
    print("Your username cannot have characters more than 14")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain numbers ")
else:
    print(f"welcome {username}")
