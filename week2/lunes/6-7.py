'''
6-7. People: Start with the program you wrote for Exercise 6-1 (page 102) .
Make two new dictionaries representing different people, and store all three dictionaries in a list called people .
Loop through your list of people . As you loop through the list, print everything you know about each person .

'''
instructor ={"first name":"Martin","last name": "Beuss", "age": 18, "city": "Hanoi"}
classmate ={"first name":"Casey","last name": "King", "age": 5, "city": "New York"}
neighbour ={"first name":"Michael","last name": "Wenz", "age": 10, "city": "Perth"}

people = [instructor,classmate, neighbour]

for each in people:
    for x in each:
        print(x, each[x])