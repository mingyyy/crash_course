'''
8-8. User Albums: Start with your program from Exercise 8-7 .
Write a while loop that allows users to enter an album’s artist and title .
Once you have that information, call make_album() with the user’s input and print the dictionary that’s created .
Be sure to include a quit value in the while loop .
'''


def make_album(name, title):
    d={}
    d[name] = title
    return d


artist=""
while artist != "martin":
    user_input = input("Please enter the artist name and album' title, separated by comma: ").split(",")
    artist = user_input[0]
    print(make_album(artist, user_input[1]))
