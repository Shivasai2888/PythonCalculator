 #Conditional expression = x if condition else Y

num = 6
a = 6
b = 7
age = 17
temperature = 17
Goals = 950
user_role = "ADMIN"
# print("Positive" if num > 0 else "Negative")
#result = "Even" if num % 2 == 0 else "ODD"
#max_num = a if a > b else b
#min_num = a if a < b else b
#status  = "ELIGIBLE FOR VOTING(ADULT)" if age >= 18 else "Not ELIGIBLE(CHILD)"
#climate = "HOT" if temperature >= 18 else "COLE PALMER"
#Goat = "Cristiano" if Goals >= 950 else "Messi"
access_level = "FULL ACCESS" if user_role == "ADMIN" else "Limited access"

print(access_level)