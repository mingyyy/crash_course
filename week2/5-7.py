'''
5-7. Favorite Fruit: Make a list of your favorite fruits,
and then write a series of independent if statements that check for certain fruits in your list .
• Make a list of your three favorite fruits and call it favorite_fruits .
• Write five if statements . Each should check whether a certain kind of fruit is in your list .
If the fruit is in your list, the if block should print a statement, such as You really like bananas!
'''

favorite_fruits = ["cherry", "durian", "loquat"]
a ="banana"
if a in favorite_fruits:
    print(f"You really love {a}!")
else:
    print(f"You don't like {a} that much.")

a="loquat"
if a in favorite_fruits:
    print(f"You really love {a}!")
else:
    print(f"You don't like {a} that much.")

a = "dragon fruit"
if a in favorite_fruits:
    print(f"You really love {a}!")
else:
    print(f"You don't like {a} that much.")

a = "apple"
if a in favorite_fruits:
    print(f"You really love {a}!")
else:
    print(f"You don't like {a} that much.")

a = "cherry"
if a in favorite_fruits:
    print(f"You really love {a}!")
else:
    print(f"You don't like {a} that much.")
