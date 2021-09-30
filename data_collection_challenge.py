"""  
replace the list used to store the values Rock, Paper and Scissors with a dictionary. Ask the user to select 1,2 or 3 to select Rock Paper or Scissors so that they no longer have to type in the word when the game starts.
"""

import random

item_list = {1: "rock", 2: "paper", 3: "scissors"}

choice = int(input("Type your selection (1-rock, 2-paper, 3-scissors): "))

randomchoice = random.choice(list(item_list.values()))


print("CPU Choice:" + randomchoice)

if item_list[choice] == "rock":
    if randomchoice == "rock":
        print("Draw")
    elif randomchoice == "paper":
        print("You lose")
    elif randomchoice == "scissors":
        print("You win")
elif item_list[choice] == "paper":
    if randomchoice == "rock":
        print("You win")
    elif randomchoice == "paper":
        print("Draw")
    elif randomchoice == "scissors":
        print("You lose")
elif item_list[choice] == "scissors":
    if randomchoice == "rock":
        print("You lose")
    elif randomchoice == "paper":
        print("You win")
    elif randomchoice == "scissors":
        print("Draw")
else:
    print("You did not enter a valid option")
