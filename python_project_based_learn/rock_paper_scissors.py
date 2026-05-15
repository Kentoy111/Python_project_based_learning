import random
options = ["rock", "paper", "scissors"]
user_options = input("Choose your move: ").lower()

def gameMove():
    computer_picked = random.choice(options)
    print(f"You picked: {user_options}")
    print(f"Computer picked: {computer_picked}")
    print(computer_picked)
    return computer_picked

computer_picked = gameMove()

if  computer_picked == "rock" and user_options == "paper":
    print("You Win ")
elif computer_picked == "rock" and user_options == "scissors":
    print("You lose") 
elif computer_picked == "paper" and user_options == "rock":
    print("You lose") 
elif computer_picked == "scissors" and user_options == "rock":
    print("You Win ")
elif computer_picked == "paper" and user_options == "scissors":
    print("You win") 
elif computer_picked == "scissors" and user_options == "paper":
    print("You Lose")          
else:
    print("Draw")
