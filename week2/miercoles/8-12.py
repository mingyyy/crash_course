'''
8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich .
The function should have one parameter that collects as many items as the function call provides,
and it should print a summary of the sandwich that is being ordered .
Call the function three times, using a different num- ber of arguments each time .
'''

def fillings(*args):
    x = ""
    for i in args:
        x += str(i)
    x = str(x)[1:-1]
    return "You have " + x + " in your sandwich."


op1 = ["turkey", "lettuce", "jam"]
print(fillings(op1))

op2 = ["ham", "lettuce", "egg", "pepper"]
print(fillings(op2))

op3 = ["apricot jam"]
print(fillings(op3))