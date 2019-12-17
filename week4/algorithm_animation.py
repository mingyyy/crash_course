import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.animation import ArtistAnimation
from random import randint
import copy

li = []
li_original = []
with open("data.txt", "r") as f:
    txt= f.read()
li=txt.split()
li = li[:100]
for i in range(len(li)):
    li_original.append(int(li[i]))
print(len(li_original), li_original)


x=[x for x in range(100)]



# Algorithm 1: bubble sort
n = int(len(li))  # 1000


# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0, 100), ylim=(0, 10000))
line, = ax.plot([], [], lw=2)


# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,


# animation function.  This is called sequentially
def animate(iii):

    for i in range(n):
        for j in range(n-i-1):
            if int(li[j])>int(li[j+1]):
                a, b=int(li[j]), int(li[j+1])
                li[j], li[j+1] = b, a
            y=li[j]
    line.set_data(x, li)
    return line,

print(len(li), li)

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=600, blit=True)

anim.save('algorithm_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()