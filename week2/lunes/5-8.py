'''
5-8. Hello Admin: Make a list of five or more usernames, including the name 'admin' .
Imagine you are writing code that will print a greeting to each user after they log in to a website .
Loop through the list, and print a greeting to each user:
• If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
• Otherwise, print a generic greeting, such as Hello Eric, thank you for log- ging in again.
'''

usernames = ['admin','end','middle','front','manager','sales','ops']
superusers =['admin', 'manager']

for i in usernames:
    if i in superusers:
        print(f"Hello {i.capitalize()}, would you like to see a status report?")
    else:
        print(f"{i.capitalize()}, thank you for loggin in again.")
