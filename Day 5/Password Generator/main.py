import random

# Character sets
char_set_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
char_set_numbers = '0123456789'
char_set_symbols = '!#$%&()*+'

print("Welcome to the Custom Password Generator!")


# Number of characters
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many special symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))


# Generate password
password_list = []

for _ in range(num_letters):
    password_list.append(random.choice(char_set_letters))

for _ in range(num_symbols):
    password_list.append(random.choice(char_set_symbols))

for _ in range(num_numbers):
    password_list.append(random.choice(char_set_numbers))


print(password_list)
print("======= \n")

random.shuffle(password_list)
generated_password = ''.join(password_list)
print(f"Your custom-generated password is: {generated_password}")
