import random

user_score = 0
computer_score = 0
score_limit = 3

while user_score != score_limit or computer_score != score_limit:
    user_action = input("rock, paper, scissors:")
    choices = ["rock", "paper", "scissors"]
    computer_action = random.choice(choices)
    print("I choose", (computer_action))
    if user_action == computer_action:
        print("draw")
    elif user_action == "rock" and computer_action == "scissors":
        print("win")
        user_score += 1
    elif user_action == "paper" and computer_action == "rock":
        print("win")
        user_score += 1
    elif user_action == "scissors" and computer_action == "paper":
        print("win")
        user_score += 1
    elif computer_action == "rock" and user_action == "scissors":
        print("win")
        computer_score += 1
    elif computer_action == "paper" and user_action == "rock":
        print("win")
        computer_score += 1
    elif computer_action == "scissors" and user_action == "paper":
        print("win")
        computer_score += 1
    if user_score >= 3:
        print("You beat me")
        print("This concludes our battle")
        break
    elif computer_score >= 3:
        print("I beat you")
        print("This concludes our battle")
        break
    print("your score", user_score, "my score", computer_score)