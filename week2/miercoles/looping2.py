locations = ["ind","spain", "mexico", "thailand"]
visited =[]

# for loc in list(locations):
#     # changing the locations while looping over it. So we have to make a copy of it by doing:
#     # list(locations) or locations.copy()
#     visited.append(locations.pop())
#
# print(locations)
# print(visited)

# more elegant solution with While loop, as long as list locations is not empty, the condition holds.
while locations:
    loc = locations.pop()
    visited.append(loc) # pop() moves by index, therefore we can't use it in the next example.
print(visited)

pets = ['cats', 'goldfish', 'dog','cats','rabbit','cats']
print(pets)
while 'cats' in pets:
    pets.remove("cats")
print(pets)