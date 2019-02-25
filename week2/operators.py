my_list = [1,2,3,4]
new_list = my_list
new_new_list = my_list.copy()

# True
print(my_list is new_list)
# False
print(my_list is new_new_list)

# Python caches small strings which works for mutable ones
# mutable ones: list, set, dictionary
# immutable ones: string, tuples (aliasing shouldn't work)




