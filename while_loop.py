"""  
# While Loop
A while loop allows code to be repeated an unknown number of times as long as a condition is being met.
=======================================================================================================
# For Loop
A for loop allows code to be repeated known number of loops/ iterations
"""
# import random
# i = 1
# while i < 6:
#     print("True")
#     i += 1
"""  
craete a programme to ask the user to guess a number between 1 - 10 and count the number of attemeted
"""
# count = 0
# num = 0
# rand = str(random.randint(1, 10))

# while num != rand:
#     num = input("Enter a number between 1-10: ")
#     count += 1

# print(rand)
# print(f"Guess count {count}")
# print("Correct!")


"""  
create a programe to genarate a random numbers and to stop the programe once number 5 found
"""
# num1 = 1
# while num1 > 0:
#     print(num1)
#     num1 = random.randint(1, 10)
#     if num1 == 5:
#         break
# print("5 was found")


# # Write a while loop that adds all the numbers from 1 to 100
# i = 1
# while i <= 100:
#     print(i)
#     i += 1

"""  
Take the following list: 
numbers=[10, 99, 98, 85, 45, 59, 65, 66, 76, 12, 35, 13, 100, 80, 95]
Using a while loop iterate through the list and for every instance of 100 print out "Found one!"
"""
# numbers = [10, 99, 100, 98, 85, 45, 59, 65,
#            100, 66, 76, 12, 100, 35, 13, 100, 80, 95]
# length = len(numbers)
# i = 0
# while i < length:
#     if numbers[i] == 100:
#         print("Found one!")

#     i += 1

"""  
Using the following list of names:
names=["Joe", "Sarah"]
Using a while loop allow users to add new names to the list indefinitely. Each time a user adds a new name ask the user if they would like to add another name. 1 = yes and 2 = no. The programme should stop if the users selects 2, no.
"""

# names = ["Joe", "Sarah"]

# while True:
#     names.append(input("Enter name: "))
#     print(names)
#     x = int(input("1-add more, 2-exit: "))

#     if x == 2:
#         break

"""  
Create a dice roll simulator whereby the user is first given an option on screen to either play or exit the simulator. An input() function is used to capture the users choice.
"""

import random
while True:
    print("1. Roll dice, \n2. Exit game")
    user = int(input("Choice 1 or 2: "))
    if user == 1:
        number = random.randint(1, 6)
        print(number)
    else:
        break
