'''
 10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop so the user can continue entering numbers
 even if they make a mistake and enter text instead of a number .
'''
ans = ""
while True and ans != ["q"]:
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
