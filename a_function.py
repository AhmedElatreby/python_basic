""" 
# Function is a block of code
# Runs when it is called
"""

# creat a function to calaulate 10% of the total bill price


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


def radius():
    user_input = int(input("Enter the radous: "))
    x = cal_area(redius1)
    print(x)
    return user_input


def area():
    radius()
    area1 = round(math.pi*(radius**2), 2)
    return area1


area()
