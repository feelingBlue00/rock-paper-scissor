import random


def userChoice():
    return input("Enter choice: (rock, paper, scissor)")


def gamePlay():
    options = ["rock", "paper", "scissor"]
    computer_choice = random.choice(options)
    player_choice = userChoice()
    computer_score = 0
    player_score = 0
    while (True):
        if (computer_choice == player_choice):
            print("Draw")
        elif player_choice == "rock":
            if computer_choice == "paper":
                computer_score += 1
            elif computer_choice == "scissor":
                player_score += 1
        elif player_choice == "paper":
            if computer_choice == "scissor":
                computer_score += 1
            elif computer_choice == "rock":
                player_score += 1
        elif player_choice == "scissor":
            if computer_choice == "rock":
                computer_score += 1
            elif computer_choice == "paper":
                player_score += 1

        play_again = input("Continue? (y/n): ")
        if play_again.lower() != "y":
            print(
                f"\nPlayer score: {player_score}\tComputer score: {computer_score} \n")
            break


gamePlay()
