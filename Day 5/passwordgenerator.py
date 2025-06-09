print("------------------------------- Welcome to Password Generator -------------------------------")

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []

#Method 1: Easy Level
# for char in range(1, nr_letters + 1):
#     random_char = random.choice(letters)
#     password += random_char
# print(password)

#Method 2: Easy Level
# for char in range(1, nr_letters + 1):
#     password += random.choice(letters)
#
# for sym in range(1, nr_symbols + 1):
#     password += random.choice(symbols)
#
# for num in range(1, nr_numbers + 1):
#     password += random.choice(numbers)
# print(password)

#Method 3: Hard Level
for i in range(nr_letters):
    password += random.choice(letters)

for i in range(nr_symbols):
    password += random.choice(symbols)

for i in range(nr_numbers):
    password += random.choice(numbers)
random.shuffle(password)

final_password = "".join(password)
print("Your final password:", final_password)
print("Thank you for using our Password Generator!")
