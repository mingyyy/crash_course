'''
10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt .
Store at least three names of cats in the first file and three names of dogs in the second file .
Write a program that tries to read these files and print the contents of the file to the screen .
Wrap your code in a try-except block to catch the FileNotFound error, and print a friendly message if a file is missing .
Move one of the files to a different location on your system,
and make sure the code in the except block executes properly .
'''

# with open("cat.txt", "a") as f:
#     f.write("Sadie\nMartin\nCaten")
#
# with open("dog.txt", "a") as f:
#     f.write("Nancy\nLucy\nCasey")

try:
    with open("cat.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            print(line)
except FileNotFoundError as err:
    print(f"Sorry, I can't find the file. {err}")

# move the dog.txt to folder: martes
try:
    with open("dog.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            print(line)
except FileNotFoundError as err:
    print(f"Sorry, I can't find the file. {err}")



