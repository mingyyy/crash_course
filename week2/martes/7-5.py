'''
7-5. Movie Tickets: A movie theater charges different ticket prices depending on a person’s age .
If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10;
and if they are over age 12, the ticket is $15 .
Write a loop in which you ask users their age, and then tell them the cost of their movie ticket .
'''
flag = True
while flag:
    a = int(input("What's your age: "))
    if a < 0:
        flag = False
    elif a < 3:
        print("The movie is FREE for you!")
    elif 3 <= a <= 12:
        print("The movie ticket is $10.")
    else:
        print("The ticket costs you $15.")
