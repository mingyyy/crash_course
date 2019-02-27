'''
8-10. Great Magicians: Start with a copy of your program from Exercise 8-9 .
Write a function called make_great() that modifies the list of magicians
by adding the phrase the Great to each magician’s name .
Call show_magicians() to see that the list has actually been modified .
'''

def show_magicians(l):
    rs = ""
    for i in l:
        rs += (i + "\n")
    return rs


l= ["Martin", "Melissa", "Michael"]
print(show_magicians(l))


def make_great(l):
    for i in range(len(l)):
        l[i] = "The Great " + l[i]
# return l

make_great(l)
print(show_magicians(l))