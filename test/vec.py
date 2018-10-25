##import matplotlib
##matplotlib.use('TkAgg')
import numpy
import tkinter as Tk

v1 = (3, -4)
v2 = (-6,4, 10)

soa = np.array([[0, 0, v1[0], v1[1]], [0, 0, v2[0], v2[1]]])
X, Y, U, V = zip(*soa)
plt.figure()
ax = plt.gca()
ax.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1)
ax.set_xlim([-10, 10])
ax.set_ylim([-5, 11])
plt.draw()

plt.show()

Tk.mainloop()

