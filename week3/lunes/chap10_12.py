'''
10-12. Favorite Number Remembered: Combine the two programs from Exercise 10-11 into one file .
If the number is already stored, report the favorite number to the user .
If not, prompt for the user’s favorite number and store it in a file . Run the program twice to see that it works .
'''

import json

filename = 'favorite.json'
with open(filename, "r") as f:
    try:
        store = json.load(f)
    except json.decoder.JSONDecodeError:
        ans = input("You favorite number please:")
        with open(filename, "w") as f:
            json.dump(ans, f)
    else:
        print("I know your favorite number! It’s " + store[0] + "!")

