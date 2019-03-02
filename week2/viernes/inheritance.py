class Food:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def buy(self, number):
        self.amount += number

    def expire(self):
        self.name = f"expired {self.name}"

    def __str__(self):
        return f"{self.amount} of {self.name}"


c = Food('carrot', 1)


class Spice(Food):
    def __init__(self, name, amount, spiciness): # this __init__ class over-writes the superclass.
        super().__init__(name, amount)
        self.spiciness = spiciness

    def __str__(self):
        super().__str__()
        return f"{self.name} is {self.spiciness}"


p = Spice("pepper", 30, "very spicy")
print(p)

p.expire()
print(p)