import numpy as np
import matplotlib.pyplot as plt

#First create some toy data:
x = np.linspace(-4, 4, 5000)
#y = 2-2*np.sin(x)+np.sin(x)*(np.sqrt(abs(np.cos(x)))/(np.sin(x)+1.4))
y = np.sqrt(np.cos(x))* np.cos(200*x)+np.sqrt(abs(x))-0.25*np.pi *((4-x**2)**0.001)
#Creates just a figure and only one subplot
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('Simple plot')
plt.show()
#TODO continue with this heart curve...
#
# #Creates two subplots and unpacks the output array immediately
# f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
# ax1.plot(x, y)
# ax1.set_title('Sharing Y axis')
# ax2.scatter(x, y)
#
# #Creates four polar axes, and accesses them through the returned array
# fig, axes = plt.subplots(2, 2, subplot_kw=dict(polar=True))
# axes[0, 0].plot(x, y)
# axes[1, 1].scatter(x, y)
#
# #Share a X axis with each column of subplots
# plt.subplots(2, 2, sharex='col')
#
# #Share a Y axis with each row of subplots
# plt.subplots(2, 2, sharey='row')
#
# #Share both X and Y axes with all subplots
# plt.subplots(2, 2, sharex='all', sharey='all')
#
# #Note that this is the same as
# plt.subplots(2, 2, sharex=True, sharey=True)
#
# #Creates figure number 10 with a single subplot
# #and clears it if it already exists.
# fig, ax=plt.subplots(num=10, clear=True)
#
