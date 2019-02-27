'''
6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers .
Think of five names, and use them as keys in your dictionary .
Think of a favorite number for each person, and store each as a value in your dictionary .
Print each person’s name and their favorite number .
For even more fun, poll a few friends and get some actual data for your program .
'''

FavNum = {"casey": 1,
          "rob": 2,
          "melissa": 7,
          "daniel": 9,
          "ben": 5}

for key in FavNum:
    print(key, FavNum[key])