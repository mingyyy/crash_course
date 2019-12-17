import matplotlib.pyplot as plt

input_values = [i for i in range(1, 6)]
squares = [i**2 for i in range(1, 6)]
plt.plot(input_values, squares, linewidth=2)
# set chart title and label axes
plt.title("Square Nubmers", fontsize=14)
plt.xlabel("Value", fontsize=10)
plt.ylabel("Square of Value", fontsize=10)
# set size of tick labels
plt.tick_params(axis='both', labelsize=8)
plt.show()
