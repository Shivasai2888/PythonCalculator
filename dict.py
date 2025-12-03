
capitals = {"USA": "WASHINGTON D.C",
            "INDIA": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(captials.get("INDIA"))

# if capitals.get("Japan"):
#    print("That capital exists")
# else:
#    print("That capital doesn't exist")

# capitals.update({"INDIA": "Hyderabad"})
# capitals.pop("China")

# capitals.popitem()

# key = capitals.keys()

# for key in capitals.keys():
#    print(key)

# values = capitals.values()

# for values in capitals.values():
#   print(values)

# items = capitals.items()

# for items in capitals.items():
#  print(items)

for key, value in capitals.items():
    print(f"for every {value} of a {key} print {value}:{key}")
