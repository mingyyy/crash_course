'''
8-9. Magicians: Make a list of magician’s names . Pass the list to a function called show_magicians(),
which prints the name of each magician in the list .
'''


def show_magicians(l):
    rs = " "
    for i in l:
        rs += (i + " ")
    return rs

print(show_magicians(["Martin", "Melissa", "Michael"]))