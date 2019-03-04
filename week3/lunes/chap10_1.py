# 10-1. Learning Python: Open a blank file in your text editor and write a few lines summarizing
# what you’ve learned about Python so far . Start each line with the phrase In Python you can... .

# Save the file as learning_python.txt in the same directory as your exercises from this chapter .
# Write a program that reads the file and prints what you wrote three times .
# Print the contents once by reading in the entire file, once by looping over the file object,
# and once by storing the lines in a list and then working with them outside the with block .

# with open("learning_python.txt") as f:
#     learn1 = f.read()
# print(learn1)


# with open("learning_python.txt") as f:
#     learn2 = f.readlines()
# for line in learn2:
#     print(line)


with open("learning_python.txt") as f:
    learn3 = f.readlines()
l = []
for line in learn3:
    l.append(line.rstrip())
print(l)