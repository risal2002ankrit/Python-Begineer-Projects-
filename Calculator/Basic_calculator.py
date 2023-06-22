# basic calcuulator
# define thee function neeeded: add, sub, mul, div
# print option to user
# ask value to user
# call the function
# while loop to continue the program untill the user wants to exit

def add(a, b):
    answer = a + b
    print(str(a) + "+" + str(b) + "=" + str(answer))


def sub(a, b):
    answer = a - b
    print(str(a) + "-" + str(b) + "=" + str(answer))


def mul(a, b):
    answer = a * b
    print(str(a) + "*" + str(b) + "=" + str(answer))


def div(a, b):
    answer = a / b
    print(str(a) + "/" + str(b) + "=" + str(answer))


while True:
    print("A.Addition")
    print("B.subtraction")
    print("C.multiplication")
    print("D.divsion")
    print("E.exit")

    choice = input('enter your choice\t')
    if choice == "a" or choice == "A":
        print("Addition")
        a = int(input("enter the 1st number"))
        b = int(input("enter the 2nd number"))
        add(a, b)
    elif choice == "b" or choice == "B":
        print("subtraction")
        a = int(input("enter the 1st number"))
        b = int(input("enter the 2nd number"))
        sub(a, b)
    elif choice == "c" or choice == "C":
        print("multiplication")
        a = int(input("enter the 1st number"))
        b = int(input("enter the 2nd number"))
        mul(a, b)
    elif choice == "d" or choice == "D":
        print("Division")
        a = int(input("enter the 1st number"))
        b = int(input("enter the 2nd number"))
        div(a, b)
    elif choice == "e" or choice == "E":
        print("Program end")
        quit()
