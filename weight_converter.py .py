# Python weight converter

weight = int(input("enter your weight :"))
unit = input("Kilograms or Pounds ? (K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs"
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs"
else:
    print(f"{unit} is not valid")

print(f"your weight is : {weight} {unit}")

