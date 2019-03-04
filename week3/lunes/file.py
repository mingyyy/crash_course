with open("recipes.txt", 'r', ) as f:
    #recipe = f.read()
    recipe = f.readlines()

for line in recipe:
    line.rstrip()
    print(line)
    for i in line.split():
        print(i)

# list comprehension
family_recipe = ["10" + line[1:].rstrip() for line in recipe]
print(family_recipe)

my_str = "hello"

with open("family_recipe.txt", "w") as fout:
    fout.write(my_str)

import markovify
# special package that create text in certain style
with open("98.txt","r") as f:
    line = f.read()
model = markovify.Text(line)
print(model.make_short_sentence(100,20))
