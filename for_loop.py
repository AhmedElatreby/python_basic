# # For Loop
# '''
# A for loop allows Python to keep repeating code a set number of times. It is sometimes known as a counting loop because you know the number of times the loop will run before it starts.
# '''
# # Code Examples
# for i in "Ahmed":
#     print(i)

# # using for loop with dictionary
# x = {1: "a", 2: "b", 3: "c"}
# for a in x.items():
#     print(a)

# # using for loop with dictionary to print two values
# x = {1: "a", 2: "b", 3: "c"}
# for c, d in x.items():
#     print(c, d)

# # using for loop with range to print 10 - 1 with drop number
# for e in range(10, 0, -1):
#     print(e)

# '''
# To stop the loop we need to use break
# '''
# for f in range(0, 10):
#     g = input("guess a number between 0 - 10: ")
#     if g == "5":
#         print("you are winner")
#         break

# '''
# Continue
# To start the next iteration
# '''
# h = (6, 9, 6, 9, 6, 9)
# for j in h:
#     if j == 6:
#         continue
#     print(j)

'''  
Nasted for loop
'''
# a = (1, 2, 3, 4)
# b = (5, 6, 7, 8)
# for i in a:
#     for y in b:
#         print(i, y)

'''  
First randomly create a number between 1-20, or your preferred range. Now let's ask the user to type in a number between the number range we have selected. The user should be given 4 turns or chances to guess the number. 
'''


# x = random.randint(1, 20)
# for i in range(0, 4):
#     y = int(input("Guess the number between (1-20): "))
#     if i == 2:
#         print("This is your last guess!...")
#     if x == y:
#         print("You guessed correctly! ")
#         print(f"The right number was {x}")
#         break
# if y != x:
#     print(f"====\nSorry! The number was {x}\n====")


# create a game to ask the user to gusse rock, paper, scissors and the winner is the best of three games
import random
item_list = {1: "rock", 2: "paper", 3: "scissors"}
ai_score = 0
user_score = 0
for x in range(0, 4):
    if ai_score == 2:
        print("=====")
        print("AI Wins")
        print("=====")
        break
    elif user_score == 2:
        print("=====")
        print("User Wins")
        print("=====")
        break
    elif x == 3:
        print("=====")
        print("The game is a draw")
        print("=====")
        break
    try:
        choice = int(
            input("Type your selection (1 - rock, 2 - paper, 3 -scissors): "))
    except ValueError:
        print("=====")
        print("You did not enter a valid option - please try again")
        print("=====")
        break

    random_choice = random.choice(list(item_list.values()))
    if item_list[choice] == random_choice:
        print("Draw")
    if item_list[choice] == "rock":
        if random_choice == "paper":
            print("You lose")
            ai_score += 1
        elif random_choice == "scissors":
            print("You win")
            user_score += 1
    elif item_list[choice] == "paper":
        if random_choice == "rock":
            print("You win")
            user_score += 1
        elif random_choice == "scissors":
            print("You lose")
            ai_score += 1
    elif item_list[choice] == "scissors":
        if random_choice == "rock":
            print("You lose")
            ai_score += 1
        elif random_choice == "paper":
            print("You win")
            user_score += 1
