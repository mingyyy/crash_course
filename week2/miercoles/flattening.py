


# while isinstance(nested_list, list):
# while type(nested_list):
# while nested_list:

# flat_list=[]
# def unpack_list(nested_list):
#     for item in nested_list:
#         if type(item) == list:
#             unpack_list(item)
#         else:
#             flat_list.append(item)
#     return flat_list

def unpack_list(nested_list, flat_list=[]):
    for item in nested_list:
        if type(item) == list:
            unpack_list(item)
        else:
            flat_list.append(item)
    return flat_list


if __name__ == '__main__':
    nested_list = [[20, 19], 1, 3, [1, 3, 4, [3, [5, 6], 4]]]
    list_ = unpack_list(nested_list)
    print(list_)




