import random
import string

print("Welcome to PyPassword Generator")

# Get user input for password requirements
count = int(input("How many letters would you like in your password?: "))
symbol = int(input("How many symbols would you like? "))
numbers = int(input("How many numbers would you like? "))

# Generate random letters, symbols, and numbers
letters = random.choices(string.ascii_letters, k=count)
symbols = random.choices(string.punctuation, k=symbol)
numbers = random.choices(string.digits, k=numbers)

# Combine all the characters together
password_list = letters + symbols + numbers

# Shuffle the password to make it random
random.shuffle(password_list)

# Join the list into a string and display the password
password = ''.join(password_list)
print(f"Your generated password is: {password}")

