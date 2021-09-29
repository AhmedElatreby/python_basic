import random

# create a random number between 1 - 10
#x = random.random()
# print(x)

# create a random int number between 1 - 100
#x = random.randint(1, 100)
# print(x)

# creat a random float number between 1 - 10
#x = random.uniform(1, 10)
# print(x)

# using rnadom range unmber with one input with 10 this mena between 0-9
#x = random.randrange(10)
# print(x)

# create a random number with evan number only between 0 and 100
#x = random.randrange(0, 101, 2)
# print(x)

# using random function with string
# x = "Ahmed"
# y = random.choice(x)
# print(y)

# using random function to select a string from list with (choice)
# item_list = ["rock", "paper", "scissors"]
# x = random.choice(item_list)
# print(x)

# using random function to select more than one number with (sample)
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# y = random.sample(x, 3)
# # * will remove []  # using sep=", " will put , and space between the numbers
# print(*y, sep=", ")

# create a game, asking the user for random number between the 1 - 10
# x = random.randrange(1, 11)
# user = int(input("please enter a number between 1 & 10: "))
# if user == x:
#     print("You have selected the correct number, welldone!")
# else:
#     print("your number didn't match, try agine")

# create a gume to ask the user to gusse rock, paper, scissors
# item_list = ["rock", "paper", "scissors"]
# choice = input("Type your selection (rock, paper, scissors): ")
# randomchoice = random.choice(item_list)
# print("CPU Choice:" + randomchoice)
# if choice == "rock":
#     if randomchoice == "rock":
#         print("Draw")
#     elif randomchoice == "paper":
#         print("You lose")
#     elif randomchoice == "scissors":
#         print("You win")
# elif choice == "paper":
#     if randomchoice == "rock":
#         print("You win")
#     elif randomchoice == "paper":
#         print("Draw")
#     elif randomchoice == "scissors":
#         print("You lose")
# elif choice == "scissors":
#     if randomchoice == "rock":
#         print("You lose")
#     elif randomchoice == "paper":
#         print("You win")
#     elif randomchoice == "scissors":
#         print("Draw")
# else:
#     print("You did not enter a valid option")

# create a lotter picker which picks and print 6 number from this list
x = [12, 26, 30, 40, 58, 6, 71, 58, 89]
y = random.sample(x, 6)
print(*y, sep=", ")
