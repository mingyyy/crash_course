a = 2
b = "zero"

# if b > a:
#     raise Exception("Whoops b is too big!")

# try:
#     result = a ** b
# except ZeroDivisionError:
#     print("Can't divide by 0.")
# except TypeError:
#     print("Please enter an number. ")
# except ValueError:
#     raise Exception("Go back and check again!")
#
# print(type(b).mro())

# project gutenberg
import logging

books = ["98.txt", "not_here.txt", "recipes.txt"]
for book in books:
    try:
        with open(book, "r") as f:
            full_text = f.read()
    except FileNotFoundError as err:
        print("sorry, this file doesn't exist:", err)
        # print(f"sorry, this file doesn't exist:{err}")
    except ValueError:
        print("oh no no..")
    else: # optional, only if no exception, the program will come here
        print(full_text[:10])
    finally: # optional, for example for file.close()
        print("always do this")



