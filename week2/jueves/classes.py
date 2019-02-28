class Ingredient:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def buy(self, num):
        self.amount += num

    def __str__(self):
        print(self.name)

    name = "carrots"
    amount = 23