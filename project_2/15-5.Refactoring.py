from random import choice
import matplotlib.pyplot as plt


class RandomWalk2():
    def __init__(self, nums=5000):
        self.nums = nums
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.nums:
            x_direction = choice([1, -1])
            x_distance = choice([i for i in range(26)])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([i for i in range(26)])
            y_step = y_direction * y_distance

            if x_step == 0 and y_step == 0:
                continue
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)