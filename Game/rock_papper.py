import random

end = False
user_point = 0
computer_point = 0


while end == False:
    options = ["rock", "paper", "scissor"]
    user_input = input("enter the rock, paper, scissor or end: ")

    if user_input == "end":
        print("game ended")
        end = True

    else:
        computer_input = random.choice(options)
        print("computer choice is : ", computer_input)

        if user_input == "rock":
            if computer_input == "rock":
                print(" Game Tie !")
            elif computer_input == "paper":
                print("you won")
                user_point += 1
            elif computer_input == "scissor":
                print("you lost")
                computer_point += 1
            else:
                break

        elif user_input == "paper":
            if computer_input == "rock":
                print(" you won !")
                user_point += 1
            elif computer_input == "paper":
                print("tie")
            elif computer_input == "scissor":
                print("you lost")
                computer_point += 1
            else:
                break

        elif user_input == "scissor":
            if computer_input == "rock":
                print(" you won")
                user_point += 1
            elif computer_input == "paper":
                print("you lost")
                computer_point += 1
            elif computer_input == "scissor":
                print("Game tie !")
            else:
                break

        elif user_input != 'rock' or user_input != 'paper' or user_input != 'scissor':
            print("Invalid input")

    print("your score is", user_point)
    print("computer score is", computer_point)
