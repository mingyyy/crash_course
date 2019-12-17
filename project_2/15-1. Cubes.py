'''
15-1. Cubes: A number raised to the third power is a cube.
Plot the first five cubic numbers, and then plot the first 5000 cubic numbers .
'''
import matplotlib.pyplot as plt

x_values = [i for i in range(1, 11)]
y_values = [i**2 for i in x_values]
# plt.scatter(x_values, y_values, c=(0, 0, 0.81), s=20)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=20)

plt.axis([0, 11, 0, 120])
plt.title('Cubes', fontsize=13)
plt.xlabel('Value', fontsize=10)
plt.ylabel('Cubes of Value', fontsize=10)
plt.tick_params(axis='both', which='major', labelsize=7)
plt.show()
