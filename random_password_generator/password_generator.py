# Ask user if they want to generate password or not
# if yes, ask for password length
#Generate password
#print password
# if inital response is no, exit program

import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():
    password_length = int(input("enter the length of password "))

    random.shuffle(characters)

    password =[]

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password= "".join(password)
    print(password)

choice = str.lower(input("Do you want to generate a password ? "))

if choice == "yes":
    generate_password()
elif choice == "no":
    print("Program ended")
    quit()
else:
    print("Invalid input, Please enter Yes or No ")
    quit()

