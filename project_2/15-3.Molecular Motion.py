import matplotlib.pyplot as plt
from RandomWalks import RandomWalk
rw = RandomWalk(50000)
rw.fill_walk()


plt.plot(rw.x_values, rw.y_values, c='red', linewidth=2)

plt.show()