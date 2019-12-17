import matplotlib.pyplot as plt
from RandomWalks import RandomWalk

# single random walk
# rw = RandomWalk(5000)
# rw.fill_walk()
# plt.scatter(rw.x_values, rw.y_values, c=rw.y_values, cmap=plt.cm.Reds,s=5)
# plt.show()

# multiple random walks
# while True:
#     rw = RandomWalk(5000)
#     rw.fill_walk()
#     plt.scatter(rw.x_values, rw.y_values, c=rw.y_values, cmap=plt.cm.Reds, s=5)
#     plt.show()
#
#     keep_running = input("Make another walk (y/n): ")
#     if keep_running == 'n':
#         break

# with styling

while True:
    rw = RandomWalk(5000)
    rw.fill_walk()

    # set the size of the plotting window
    plt.figure(dpi=128, figsize=(10, 6))

    point_numbers = list(range(rw.nums))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=3)

    # Emphasize the fist and last point
    plt.scatter(0,0,c='green', edgecolors=None, s=15)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors=None, s=12)

    # Remove the axes
    plt.axes().get_yaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()
    keep_running = input("Make another walk (y/n): ")
    if keep_running == 'n':
        break