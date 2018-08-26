import matplotlib.pyplot as plt
import numpy as np

def x(t):
    return 16*np.sin(t) ** 3

def y(t):
    return 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

t = np.arange(0,2*np.pi,0.01)
right_t = np.pi/2
right_y = y(right_t)
x = x(t)
y = y(t)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xlim(-17,17)
ax.set_ylim(-20,13)
ax.plot(x,y,color = 'pink')
ax.fill_between(x,y,y2=right_y,color='red')
ax.set_aspect(1)

plt.show()