'''
3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner,
so you need to send out a new set of invitations . You’ll have to think of someone else to invite .
• Start with your program from Exercise 3-4 .
  Add a print statement at the end of your program stating the name of the guest who can’t make it .
• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still in your list .
'''
from week1.GuestList import guests
x=""
for i in guests:
    x += i +" "
print(f"{x}can't make it to the dinner.")

newlist = guests[-2:]
newlist.insert(0, "Michael Jordan")

# for i in newlist:
#     print(f"Dear {i}, It would be my honor to have you for dinner tonight."
#           f"\n\t Address: Jalan Nuyh Kuning 04\n\t Friday 7PM")

'''
 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 through 3-7 (page 46),
      use len() to print a message indicating the number of people you are inviting to dinner .
'''

print(f"{len(newlist)} guests are invited.")

