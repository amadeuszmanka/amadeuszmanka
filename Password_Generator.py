import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to Password Generator!")
user_choice = input("What kind of password do you want to generate? STRONG or SUPERSTRONG? \n")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#strong password
if user_choice.lower() == "strong":
    password = []
    for letter in range(nr_letters):
        password.append(random.choice(letters))
    for symbol in range(nr_symbols):
        password.append(random.choice(symbols))
    for number in range(nr_numbers):
        password.append(random.choice(numbers))

    password = "".join(password)

    print(f"Your new password can be: {password}")


#superstrong password
else:
    stronger_password = []
    for letter in range(nr_letters):
        stronger_password.append(random.choice(letters))
    for symbol in range(nr_symbols):
        stronger_password.append(random.choice(symbols))
    for number in range(nr_numbers):
        stronger_password.append(random.choice(numbers))

    random.shuffle(stronger_password)

    stronger_password = "".join(stronger_password)

    print(f"Your new password can be: {stronger_password}")


