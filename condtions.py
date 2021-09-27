# This is a Password matching application
x = "notsafe"
y = "Ahmed"
name = input("please enter your username:")
password = input("please enter your password:")

if password == x and name == y:
    print(f"{y} have enterd the correct password")
    print(f"{y} can access the securet code now!")
else:
    print(f"you enterd incoret password or username")

# This a coin levels application
x = int(input("please enter the number of coins: "))

if x >= 0 and x <= 20:
    print("You are Bronze level")
elif x >= 21 and x <= 40:
    print("You are a Silver level")
elif x >= 41:
    print("You have Gold level")
else:
    print("Please enter a valid input")

# Pizza slice calculator
pizza = int(12)
z = int(input("Enter the number of pizza slices that you eaten: "))
total = pizza - z
if z >= 0 and z <= 12:
    print(f"the number of pizza remaing are {total}")
else:
    print("Please enter a vaild a mount")
