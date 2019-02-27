# How to create a empty dictionary:
dict_1 = dict()
dict_2 = {}
print(dict_1)

# how to make a new dictionary:
# {key: value, another item, another key value pair}
recipe ={'carrots': 4, 'apple': 10, 'water': 1}
#print(recipe)

students = [{'name': 'fred',
                'age': 21,
                'nationality': ['German','Indonesia'],
                'student_ID': 1},
            {'name': 'melissa',
                'age': 18,
                'nationality': 'NZ',
                'student_ID': 2},
            {'name': 'casey',
             'age': 10,
             'nationality': 'United States',
             'student_ID': 3}
            ]


#print(students[0]["nationality"][0])

for student in students:
    if student['age'] > 18:
        print(student["name"].capitalize() + " can go out with Martin.")

# change a value in dictionary
students[1]['nationality'] = 'New Zealand'
print(students[1])

# if it wasn't there before. it will be created.
students[1]['Residence'] = 'New York'
print(students[1])

# delete a pair
# del students[1]['Residence']
# or pop the key

home = students[1].pop('Residence')
print(home)


# tuple unpacking
t = 1, 2
a, b = t
print(a,b)