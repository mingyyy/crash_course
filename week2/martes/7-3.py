'''7-3.
Multiples of Ten: Ask the user for a number, and then report whether the number is a multiple of 10 or not .
'''

num = int(input("Please give me a number: "))
if num % 10 ==0:
    print(f"{num} is a multiple of 10.")
else:
    print(f"{num} is NOT a multiple of 10.")
