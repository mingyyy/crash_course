import matplotlib.pyplot as plt

x_value = [i for i in range(1, 101)]
y_value = [i**2 for i in x_value]

# plt.scatter(x_value, y_value, c=(0,0,0.81), edgecolors=None, s=10)
# using colormap which is a series of colors in a gradient
plt.scatter(x_value, y_value, c=y_value,cmap=plt.cm.Blues, edgecolors=None, s=10)

# set the range for each axis
plt.axis([0, 110, 0, 11000])

plt.title("Square Numbers", fontsize=14)
plt.xlabel("Value", fontsize=10)
plt.ylabel("Square of Value", fontsize=10)

plt.tick_params(axis='both', which='major', labelsize=8)

# saving plot automatically
plt.savefig('squares_plot.png', bbox_inches='tight')
plt.show()