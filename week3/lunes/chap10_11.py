'''
10-11. Favorite Number: Write a program that prompts for the user’s favorite number .
Use json.dump() to store this number in a file .
Write a separate program that reads in this value and prints the message, “I know your favorite number! It’s _____ .”
'''
import json

ans = input("Your favorite number please:")
filename = 'favorite.json'
with open(filename, 'w') as f:
   json.dump(ans, f)

print("I know your favorite number! It’s " + ans + "!")
