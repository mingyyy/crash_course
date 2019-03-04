'''
10-6. Addition: One common problem when prompting for numerical input occurs when people provide text instead of numbers .
When you try to convert the input to an int, you’ll get a TypeError . Write a program that prompts for two numbers .
Add them together and print the result . Catch the TypeError if either input value is not a number,
and print a friendly error message .

Test your program by entering two numbers and then by entering some text instead of a number .

'''
s = 0
try:
    ans = input("Tell me your two of your favorite integers, please (separated by ,): ").split(",")
    for i in ans:
        s += int(i)
except TypeError:
    print("You need to key in a number e.g. 1.")
except ValueError:
    print("You should enter a number e.g. 1.")
else:
    print(s)
finally:
    print(f"You entered {ans}, and you get {s}")
