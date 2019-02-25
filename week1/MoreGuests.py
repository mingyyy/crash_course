'''
3-6. More Guests: You just found a bigger dinner table, so now more space is available .
Think of three more guests to invite to dinner .
• Start with your program from Exercise 3-4 or Exercise 3-5 .
Add a print statement to the end of your program informing people that you found a bigger dinner table .
• Use insert() to add one new guest to the beginning of your list .
• Use insert() to add one new guest to the middle of your list .
• Use append() to add one new guest to the end of your list .
• Print a new set of invitation messages, one for each person in your list .
'''

from week1 import GuestList

GuestList.guests.insert(0, "Dan Brown")
GuestList.guests.insert(2, "Paolo Cuelo")
GuestList.guests.append("Chris Sharma")


for i in GuestList.guests:
    print(f"Dear {i}, It would be my honor to have you for dinner tonight."
          f"\n\t Address: Jalan Nuyh Kuning 04\n\t Friday 7PM")

'''

3-10. Every Function: Think of something you could store in a list . 
For example, you could make a list of mountains, rivers, countries, cities, languages, or any- thing else you’d like . 
Write a program that creates a list containing these items and then uses each function introduced in this chapter 
at least once .
'''

languages = ["spanish","french", "arabic"]

languages.sort()
print(languages)

languages.reverse()
