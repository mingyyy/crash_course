'''
 6-8. Pets: Make several dictionaries, where the name of each dictionary is the name of a pet .
 In each dictionary, include the kind of animal and the owner’s name .
 Store these dictionaries in a list called pets .
 Next, loop through your list and as you do print everything you know about each pet .
'''

lila = {"kind": "dog", "owner": "sarah"}
lady = {"kind": "dog", "owner": "may"}
babe = {"kind": "cat", "owner": "chantelle"}
coco = {"kind": "pig", "owner": "lucky"}
pets = [babe, coco, lady, lila]

s = []
for i in dir():
    if len(i) == 4 and i != "pets":
        s.append(i.capitalize())
s.sort()
n = 0
for each in pets:
    n += 1
    print(list(each.values())[1].capitalize() + " is the " + list(each.keys())[1] + " of a " + list(each.values())[0] + " called " + s[n-1]+".")


