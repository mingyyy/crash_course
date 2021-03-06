'''
10-13. Verify User: The final listing for remember_me.py assumes either that the user has already entered their username
or that the program is running for the first time .
We should modify it in case the current user is not the person who last used the program .
Before printing a welcome back message in greet_user(), ask the user if this is the correct username .
If it’s not, call get_new_username() to get the correct username .

'''
import json

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """Greet the user by name."""
    filename = 'username.json'
    try:
        with open(filename,"r") as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you come back, " + username + "!")
    else:
        ans = input(f"Hi there, is your username: {username}? (Y/N): ")
        if ans.upper() == "Y":
            print("Welcome back, " + username + "!")
        else:
            new = get_new_username()
            print(f"Welcome! {new}, we'll remember you when you come back!")


greet_user()
