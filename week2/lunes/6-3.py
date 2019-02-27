'''
6-3. Glossary: A Python dictionary can be used to model an actual dictionary .
However, to avoid confusion, let’s call it a glossary .
• Think of five programming words you’ve learned about in the previous chapters .
Use these words as the keys in your glossary, and store their meanings as values .
• Print each word and its meaning as neatly formatted output .
You might print the word followed by a colon and then its meaning,
or print the word on one line and then print its meaning indented on a second line .
Use the newline character (\n) to insert a blank line between each word-meaning pair in your output .

'''

glossary = {"List": "collections of information in variables called lists",
            "Slicing": "to work with a specific group of items in a list is called slicing",
            "Conditional test": "At the heart of every if statement is an expression that can be evaluated as True or False",
            "Tuples": "values that cannot change as immutable, and an immutable list is called a tuple",
            "PEP": "Python Enhancement Proposal"}

for key in glossary:
    print(f"{key} in Python means {glossary[key]}\n")

for key in glossary:
    print(f"{key}: \n    in Python it means {glossary[key]}\n")