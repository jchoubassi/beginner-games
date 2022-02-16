import random

user_wins = 0
comp_wins = 0

options = ["Rock", "Paper", "Scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock = 0, paper = 1, scissors = 2
    comp_pick = options[random_number]
    print("Computer picked", comp_pick + ".")

    if user_input == "rock" and comp_pick == "scissors":
        print("You win!")
        user_wins += 1
    
    elif user_input == "paper" and comp_pick == "rock":
        print("You win!")
        user_wins += 1
        
    elif user_input == "scissors" and comp_pick == "paper":
        print("You win!")
        user_wins += 1
        
    else:
        print("You lost!")
        comp_wins += 1

print("You won", user_wins, "times")
print("You won", comp_wins, "times")
print("Goodbye!")


