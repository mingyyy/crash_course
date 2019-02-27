'''
6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102)
so each person can have more than one favorite number .
Then print each person’s name along with their favorite numbers .
'''

FavNum = {"casey": [1,3,5],
          "rob": 2,
          "melissa": [7,8],
          "daniel": 9,
          "ben": [5,23,31,47]}

for name, n in FavNum.items():
    if type(n) == list:
        print(name.capitalize() + "'s favorite numbers are", end = " ")
        for i in n:
            print(i, end= " ")
        print(".")

    else:
        print(f"{name.capitalize()}'s favorite number is {n}.")

