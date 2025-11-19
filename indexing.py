"""Program to mask credit card number"""

credit_number = "1234-7456-8912"

# print(credit_number[0])
# print(credit_number[:4])
# print(credit_number[5:9])
# print(credit_number[5:])
# print(credit_number[-2])
# print(credit_number[::3])
# print(credit_number[10:])
credit_number = credit_number[::-1]

last_digits = credit_number[-4:]

print(f"Your credit card number is XXXX-XXXX-{last_digits} ")
