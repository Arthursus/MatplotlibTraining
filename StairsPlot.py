import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot()
x1 = np.arange(0, 10)
ax.step(x1, x1, '-go', x1, np.cos(x1), '--x', where='mid')
ax.grid()
plt.show()

fig = plt.figure(figsize=(5, 4))
ax = fig.add_subplot()
x2 = np.arange(-2, 2, 0.1)
y1 = np.array([-y**2 for y in x2]) + 8
y2 = np.array([-y**2 for y in x2]) + 8
y3 = np.array([-y**2 for y in x2]) + 8
ax.stackplot(x2, y1, y2, y3)
ax.grid()
plt.show()

fig = plt.figure(figsize=(6, 4))
ax = fig.add_subplot()
x3 = np.arange(-np.pi, np.pi, 0.3)
ax.stem(x3, np.cos(x3), '--r', '^g', ':', bottom=0.5)
ax.grid()
plt.show()
