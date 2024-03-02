import random

def get_choice():
  things=["rock", "paper", "scissors"]
  player_choice=input("Enter a choice (rock, paper, scissors): ")
  computer_choice=random.choice(things)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices
  
def check_win(player, computer):
  print(f"You chose {player} and  computer chose {computer}")

  if player == computer:
    return "its a tie!"

  elif player == "rock": 
    if computer == "scissors":
      return "Rock smashes scissors! You win!"
    else:
      return "Paper covers rock! You lose."
    
  elif player == "paper": 
    if computer == "scissors":
      return "Scissors cuts the paper! You lose!" 
    else :
      return "Paper covers rock! You win."

  elif player == "scissors": 
    if computer == "rock":
      return "Rock smashes scissors! You loose!"
    else :
      return "Scissors cuts the paper! You win."

choices = get_choice()
result = check_win(choices["player"], choices["computer"])
print(result)