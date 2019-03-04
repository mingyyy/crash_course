'''
10-4. Guest Book: Write a while loop that prompts users for their name .
When they enter their name, print a greeting to the screen and
add a line recording their visit in a file called guest_book.txt .
Make sure each entry appears on a new line in the file .
'''
name = ""
with open("guest_book.txt", "a") as f:
    while True and name != "Ming":
        name = input("Tell me your name please: ")
        print(f"Welcome to Outpost, {name}")
        f.write(name + "\n")
