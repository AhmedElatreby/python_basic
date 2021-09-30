""" 
# Tuple is a collection that is:
- Written in round brackets()
- ordered
- immutable (cannot be changed)
- items are index
"""
# you can not change tuple
item = (False, 1, "scissoes")
print(item.index(1))

# create a loop with a tuple
for x in item:
    print(x)

# you cannot reassign tuple, but you can override it
item = (1, 2, 3, 4, 5, 6)
for x in item:
    print(x)
