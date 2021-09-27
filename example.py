# x = input("Enter your name: ")
# y = input("Enter your age: ")
# print(f"{x} is {y}")

# pizza = int(12)
# z = input("Enter the number of pizza slices that you eaten: ")
# total = (pizza-int(z))
# print(f"the number of pizza remaing are {total}")

# create customer bill calculator
customer = input("Please enter you name: ")
bill = input("Please enter your bill ")
bill_after_tax = format(float(bill) / 10 + float(bill), '.2f')
print(
    f"customer name is: {customer} \nbill befor tax: {bill} bill after tax {bill_after_tax}")
