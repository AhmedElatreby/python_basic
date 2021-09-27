# ex5.0.4 Order of operations
# B - Brackets first
# O - Orders(i.e. Powers and Square Roots, etc.)
# DM - Division or Multiplication(left-to-right)
# AS - Addition or Subtraction(left-to-right)

# print(1+10*10)  # M-A = 101
# print(10*1+10)  # M-A = 20
# print(10*(1+10))  # B-M = 110
# print(10/2*(1+10))  # B-D-M = 55

# code challenge 1 round pi to 2 numbers
import math

x = math.pi
print(format(x, '.2f'))
# challenge 2 the user will input a price of product and the programme should calculate the price minus sales 20%
# x = float(input("Please input product price: "))
# y = x * 20 / 100
# z = x - y
# print(
#     f"the total of prodect pefore discount is £{x} product after discount is £{z}")

# challange 3 create simple calculator
x = float(input("Please enter your first number: "))
y = float(input("Please enter your secound number: "))
z = input("Please enter +, - / or *: ")

if z == "+":
    print(format(x + y))
elif z == "-":
    print(format(x - y))
elif z == "/":
    print(format(x / y))
elif z == "*":
    print(format(x * y))
else:
    print("Please enter correct value")
