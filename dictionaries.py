"""  
Dictionaries
Adictionary is a collection of data that is:
- Written with curly brackets, and have keys and values:
- Uesd to sorte data values in key: value pairs
- An ordered collection
- Does not allow duplicates
"""
dictionary = {1: "rock", 2: "paper", 3: "scissors"}
print(dictionary)
print(type(dictionary))
print(type(dictionary[3]))
print(dictionary[1])
print(dictionary[2])
print(dictionary[3])

"""
unlike Tuple in Dictionaries you can chainge the list
"""
dictionary[1] = "Ahmed"
print(dictionary)

"""  
You can added more into dictionary by using update
"""
dictionary.update({4: "hi", 5: "Hello World!"})
print(dictionary)

"""  
to remove data form dictionary we use pop followed by num of the list in dictionary than None
"""
dictionary.pop(2, None)
print(dictionary)
