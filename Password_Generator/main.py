import random
import string

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []

for letter in range(0, nr_letters):
    password_list.append(random.choice(string.ascii_letters))

for symbol in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

for number in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ''

for char in password_list:
    password += char

print(f'Your password is {password}')
