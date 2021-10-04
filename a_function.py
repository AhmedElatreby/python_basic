""" 
# Function is a block of code
# Runs when it is called
"""

# creat a function to calaulate 10% of the total bill price


import sys
import math


def get_bill_total():
    bill_total = float(input("Enter the total: "))
    return bill_total


def main():
    total = get_bill_total()
    discount = total - total / 100 * 10
    final_price = format(discount, '.2f')
    print("£" + final_price)


main()


# create a function to calculate the radius


def cal_area(rad):
    user_input = round(math.pi*(rad**2), 2)
    return user_input


def area():
    radius = int(input("Enter the radius: "))
    x = cal_area(radius)
    print(x)


area()
"""  
Change amount of discount applied based upon the amount spent. For example if the customer spends 100 or more the discount applied should be 20% if the customer spends less than 100 the discount applied should be 10%
Use Try/Except to capture if the user accidentally types in the wrong input
"""
# Original Code


def calculate_discount_20(total):
    discount = total - total / 100 * 20
    return discount


def calculate_discount_10(total):
    discount = total - total / 100 * 10
    return discount


def get_bill_total():
    bill_total = float(input("Enter the amount: "))
    if bill_total >= 100:
        final_total = format(calculate_discount_20(bill_total), '.2f')
    elif bill_total < 100:
        final_total = format(calculate_discount_10(bill_total), '.2f')
        if bill_total < 1:
            print("Please enter a valed input")

    else:
        print("Please enter a valed input")
    return final_total


def main1():
    total = get_bill_total()
    print("£" + total)


main1()

# Challenge 2 - Cost Calculation Solutions


def calculate_discount_percentage(total):
    if total >= 100:
        discount = 20
    elif total > 0 and total < 100:
        discount = 10
    return discount


def calculate_discount(total):
    discount_percentage = calculate_discount_percentage(total)
    discount = total - total / 100 * discount_percentage
    return discount


def get_bill_total():

    try:
        bill_total = float(input("Enter the amount: "))
    except ValueError as e:
        print('Incorrect value entered')
        # quit() This function (callable instance objects) should only be used in the interpreter.
        # exit()
        sys.exit()

    if bill_total < 1:
        print('Incorrect value entered')
        sys.exit()

    final_total = format(calculate_discount(bill_total), '.2f')
    return final_total


def main():
    total = get_bill_total()
    print("£" + total)


main()
