'''
8-11. Unchanged Magicians: Start with your work from Exercise 8-10 .
Call the function make_great() with a copy of the list of magicians’ names .
Because the original list will be unchanged, return the new list and store it in a separate list .
Call show_magicians() with each list to show that you have one list of the original names
and one list with the Great added to each magician’s name .'''


def show_magicians(l):
    rs = ""
    for i in l:
        rs += (i + "\n")
    return rs


l= ["Martin", "Melissa", "Michael"]
print(show_magicians(l))


def make_great(l):
    x = l.copy()
    for i in range(len(l)):
        x[i] = "The Great " + l[i]
    return x

print(make_great(l))
print(show_magicians(l))