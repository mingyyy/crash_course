from random import randint
import pygal


class Die():
    def __init__(self, num_sides=6):
        # dice of 6 sides
        self.num_sides = num_sides

    def roll(self):
        # return a random value between 1 and the number of sides
        return randint(1, self.num_sides)


n = 10000
m = 3
d1 = 6
d2 = 6
d3 = 6
die1 = Die(d1)
die2 = Die(d2)
die3 = Die(d3)
results = []
for roll_num in range(n):
    results.append(die1.roll() + die2.roll() + die3.roll())
# print(results)

freq = []

for value in range(m, die1.num_sides + die2.num_sides + die3.num_sides + 1):
    freq.append(results.count(value))
# print(freq)

# visualize the results
hist = pygal.Bar()
hist.title = f"Results of rolling three D{die1.num_sides} {n} times"
# 15-6, list comprehension
hist.x_labels = [i for i in range(1*m, d1+d2+d3+1)]
hist.x_title = "Results"
hist.y_title = "Frequency of Result"

hist.add(f'D{d1} + D{d2} + D{d3}', freq)
# save to the current folder, open the svg with a browser
hist.render_to_file(f'dice_visual_{m}{d1}{d2}{d3}.svg')