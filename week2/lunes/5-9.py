'''
5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty .
• If the list is empty, print the message We need to find some users!
• Remove all of the usernames from your list, and make sure the correct
message is printed .
'''

usernames = [] #['admin','end','middle','front','manager','sales','ops']
superusers =['admin', 'manager']

if usernames: # if the list is empty Python returns a False, otherwise True
    for i in usernames:
        if i in superusers:
            print(f"Hello {i.capitalize()}, would you like to see a status report?")
        else:
            print(f"{i.capitalize()}, thank you for loggin in again.")
else:
    print("We need to find some users!")