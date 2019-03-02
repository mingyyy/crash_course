'''
9-13. OrderedDict Rewrite: Start with Exercise 6-4 (page 108),
where you used a standard dictionary to represent a glossary .
Rewrite the program using the OrderedDict class and
make sure the order of the output matches the order in which key-value pairs were added to the dictionary .
'''
# glossary from 6-4
# glossary = {"List": "collections of information in variables called lists",
#             "Slicing": "to work with a specific group of items in a list is called slicing",
#             "Conditional test": "At the heart of every if statement is an expression that can be evaluated as True or False",
#             "Tuples": "values that cannot change as immutable, and an immutable list is called a tuple",
#             "PEP": "Python Enhancement Proposal"}
# for k in sorted(glossary.keys()):
#     print(f"{k} in Python means:\n    {glossary[k].capitalize()}")


class OrderedDict:
    glossary = {}

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f"{self.key} in Python means:\n    {self.value.capitalize()}"

    def append_item(self):
        self.glossary[self.key] = self.value


item1 = OrderedDict("List","collections of information in variables called lists")
item1.append_item()
item2 = OrderedDict("Slicing","to work with a specific group of items in a list is called slicing")
item2.append_item()
item3 = OrderedDict("Conditional test", "At the heart of every if statement is an expression that can be evaluated as True or False")
item3.append_item()

print(OrderedDict.glossary)
print(item1)
print(item2)
print(item3)
