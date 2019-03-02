'''
6-4. Glossary 2: Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 102)
by replacing your series of print statements with a loop that runs through the dictionary’s keys and values .
When you’re sure that your loop works, add five more Python terms to your glossary .
When you run your program again, these new words and meanings should automatically be included in the output .
'''

glossary = {"List": "collections of information in variables called lists",
            "Slicing": "to work with a specific group of items in a list is called slicing",
            "Conditional test": "At the heart of every if statement is an expression that can be evaluated as True or False",
            "Tuples": "values that cannot change as immutable, and an immutable list is called a tuple",
            "PEP": "Python Enhancement Proposal"}

for key, value in glossary.items():
    print(f"{key}: \n    in Python it means {value}\n")