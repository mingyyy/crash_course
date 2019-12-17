from random import choice
import matplotlib.pyplot as plt


class RandomWalk2():
    def __init__(self, nums=5000):
        self.nums = nums
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.nums:
            x_step = self.get_step()
            y_step = self.get_step()
            if x_step == 0 and y_step == 0:
                continue
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def get_step(self):
        direction = choice([1,-1])
        distance = choice([i for i in range(6)])
        step = direction * distance
        return step


rw = RandomWalk2(5000)
rw.fill_walk()

plt.plot(rw.x_values, rw.y_values, c='red', linewidth=1)
plt.show()