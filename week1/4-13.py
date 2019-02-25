'''
4-13. Buffet: A buffet-style restaurant offers only five basic foods .
Think of five simple foods, and store them in a tuple .
• Use a for loop to print each food the restaurant offers .
• Try to modify one of the items, and make sure that Python rejects the
change .
• The restaurant changes its menu, replacing two of the items with different foods .
Add a block of code that rewrites the tuple, and then use a for loop to print each of the items on the revised menu .
'''

# a Indonesian menu
menu = "mie goreng", "satay", "nasi goreng", "redang", "gado gado"

for i in menu:
    print(i)

# menu[1] = "ayam"
menu_new = list(menu)
menu_new[0] = "ayam"
menu_new[2] = "ikan"
new_menu = tuple(menu_new)

for i in new_menu:
    print(i)

# we can also create a new tuple from the slicing the existing one
# then we add two new items in that new tuple
print()

for food in new_menu:
    if food == "ayam":
        print("I like to eat chicken!")
    elif food == "ikan":
        print("I like fish even more!")
    else:
         print("ahhhh")