import numpy as np
import matplotlib.pyplot as plt
from random import randint
import copy

# flip the list
# li=[8,6,2,5]
# n=int(len(li))
# m=int(n/2)
# for i in range(int(m)):
#     a=li[i]
#     e=li[n-1-i]
#     li[i]=e
#     li[n-1-i]=a
#
# print(li)

# Creat the data list in data.txt
# with open("data.txt", "w") as f:
#     for i in range(1000):
#         f.write(f"{randint(0,10000)} ")

# read in the data.txt file into a list: li
li = []
li_original = []
with open("data.txt", "r") as f:
    txt= f.read()
li=txt.split()
li = li[:100]
print(li)
for i in range(len(li)):
    li_original.append(int(li[i]))
print(len(li_original), li_original)

x=[x for x in range(100)]

# Algorithm 1: bubble sort
n = int(len(li)) # 1000

for i in range(n):
    for j in range(n-i-1):
        if int(li[j])>int(li[j+1]):
            a, b=int(li[j]), int(li[j+1])
            li[j], li[j+1] = b, a

print(len(li), li)

# Algorithm 2: grouping

# for i in range(0,n,2):


fig, ax = plt.subplots()

# plt.title("random 1000")
# plt.xlabel("x-axis")
# plt.ylabel("random numbers(1-1000)")
# plt.bar(x, li)
# plt.show()


index = np.arange(100)
bar_width = 0.35

opacity = 0.4
error_config = {'ecolor': '0.3'}

rects1 = ax.bar(index, li, bar_width,
                alpha=opacity, color='b',
                error_kw=error_config,
                label='Sorted')

rects2 = ax.bar(index + bar_width, li_original, bar_width,
                alpha=opacity, color='r',
                 error_kw=error_config,
                label='Unsorted')

ax.set_xlabel('1 to 100')
ax.set_ylabel('numbers')
ax.set_title('Sorting Algorithm - bubble search')
# ax.set_xticks(index + bar_width / 2)
# ax.set_xticklabels(('A', 'B', 'C', 'D', 'E'))
ax.legend()

fig.tight_layout()
plt.show()