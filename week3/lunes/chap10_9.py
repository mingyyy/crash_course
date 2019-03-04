'''
10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail silently if either file is missing .
'''

# move the dog.txt to folder: martes
try:
    with open("dog.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            print(line)
except FileNotFoundError as err:
    pass

try:
    with open("cat.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            print(line)
except FileNotFoundError:
    pass