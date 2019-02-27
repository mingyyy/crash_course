'''6-1. Person: Use a dictionary to store information about a person you know .
Store their first name, last name, age, and the city in which they live .
You should have keys such as first_name, last_name, age, and city .
Print each piece of information stored in your dictionary .'''

instructor ={"first name":"Martin","last name": "Beuss", "age": 18, "city": "Hanoi"}

# by defult it will loop over the keys
for key in instructor:
    print(key, str(instructor[key]))

# another method to get a list of keys and values, but it's not a list but a 'dict_keys' or 'dict_value'
# it is iterables
print(instructor.keys())
print(list(instructor.values())[0])
# type dict_items will give us a number tuples
print(instructor.items())
# sort the items before the iteration
for k, v in sorted(instructor.items()):
    print(f"{k} is {v}")
    print(type(k[0]))
