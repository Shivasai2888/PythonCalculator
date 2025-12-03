"""Program to demonstrate Python format specifiers"""


price1 = 3.14159
price2 = -987.65
price3 = 1200.3499
price4 = 223.90
price5 = 99.9
price6 = 60000.889

print(f"Price 1 is ${price1:10}")
print(f"Price 2 is ${price2:010}")
print(f"Price 3 is ${price3: .2f}")
print(f"Price 4 is ${price4: ^10}")
print(f"Price 4 is ${price5: >10}")
print(f"Price 4 is ${price3:+}")
print(f"Price 4 is ${price6:,}")
print(f"Price 3 is ${price3:+,.2f}")
