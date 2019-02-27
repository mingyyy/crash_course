'''
7-2. Restaurant Seating: Write a program that asks the user how many people are in their dinner group .
If the answer is more than eight, print a message say- ing they’ll have to wait for a table .
Otherwise, report that their table is ready .
7-3. Multiples of Ten: Ask the user for a number, and then report whether the number is a multiple of 10 or not .
'''

pro = int(input("How many people are there in your dinner group? "))
if pro > 8:
    print("They'll have to wait for a table.")
else:
    print("Their table is ready.")