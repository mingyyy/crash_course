'''
 7-6. Three Exits: Write different versions of either Exercise 7-4 or
 Exercise 7-5 that do each of the following at least once:
• Use a conditional test in the while statement to stop the loop .
• Use an active variable to control how long the loop runs .
• Use a break statement to exit the loop when the user enters a 'quit' value .
'''

# conditional
topping = ''
while topping != 'pizza':
    topping = input("Please enter your pizza topping: ")
    print(f"You will add {topping} to your pizza. ")

# active variable:
active = True
while active:
    topping = input("Please enter your pizza topping: ")
    if topping == "martin":
        active = False
    print(f"You will add {topping} to your pizza. ")

# break
topping = ''
while topping != ' ': # one space
    topping = input("Please enter your pizza topping: ")
    if topping == "quit":
        break
    print(f"You will add {topping} to your pizza. ")



