# ask the user to input their password and user name
# using len funtion to check password count
# x = input("Please enter your name: ")
# y = input("please enter your password: ")
# z = input("please enter your password again: ")

# if y == z:
#     if len(y) < 8 or len(z) < 8:
#         print("your password need to be more than 8 characters")
#     else:
#         print("Thank you, your account has been created")
# else:
#     print("Your password does not match")
#     print("Please enter your password again")


# ask the user for their phone unmber and display
# the last 3 number and the rest of their number replaced with *
# x = input("please enter your phon number: ")
# y = len(x) - 3
# z = x[-3:]
# print(("*")*y + z)

# ask user to input heir first and last name
# print ther initials
# x = input("please enter your First name: ")
# y = input("please enter your Surname: ")
# fn = x[:1]
# ln = y[:1]
# print((fn+ln).upper())


# Use the list shown below to count the number of instances the number 10 occurs. Calculate the combined total
# x = [10, 1, 12, 42, 51, 1010, 124, 10, 23, 10, 42, 52, 3, 10]
# y = x.count(10)
# z = y * 10
# print(z)

# Ask the user to type in their name. If their name matches a name is the provided list let the user know. If their name does not match any names in the list capture the ValueError and print a suitable message.
x = ["Smaith", "Ahmed", "Mark"]
y = input("Please enter your name: ")
try:
    x.index(y)
    print("You have enter the correct name")
except ValueError:
    print("you have enter the wrong name, keep guessing")
