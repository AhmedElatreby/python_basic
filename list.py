""" 
List
A list is a collection of data that is:
- Written in square brackets[]
- Ordered
- Changeable
- List item are index
"""
item = ["rock", "paper", "scissors"]
print(item)
print(item[0])
print(item[1])
print(item[2])
print(item.index("rock"))

# To check the length of the list
print(len(item))

# To build a list we need to use list followed by ()
item_1 = list((1, True, 5, "hi", "Hello World!", "Ahmed"))
print(item_1)
# To display the type of list we need to use type
print(type(item_1))
# you can you slices with list to input a spicific part
print(item_1[0:3])
# using if condtion with list
if "Ahmed" in item_1:
    print(f"Hello {item_1[-1]}")
else:
    print("try again")

"""
unlike Tuple in list you can chainge the list
"""
item_1[0] = 99
print(item_1)

""" 
remove item from a list
"""
item_1.remove("hi")
print(item_1)

""" 
We use append to add item to the list
"""
item_1.append("This is a new item using APPEND")
print(item_1)

""" 
We use insert to add item to the list in a specifc location
first value is the location, secound value is the item
"""
item_1.insert(1, "new item using INSERT")
print(item_1)
# using loop to disply list
for x in item_1:
    print(x)
""" 
using sorted to order the list 
"""
list1 = ["a", "h", "f", "r", "v", "z", "e"]
list2 = [9, 6, 5, 8, 4, 1, 66, 7, 0, 4]
print(sorted(list1))
print(sorted(list2))
