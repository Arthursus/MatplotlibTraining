import matplotlib.pyplot as plt
import numpy as np

fig1 = plt.figure(figsize=(4, 4))
ax1 = fig1.add_subplot()
x1 = np.arange(0, 10)
ax1.step(x1, x1, '-go', x1, np.cos(x1), '--x', where='mid')
ax1.grid()
fig1.show()

fig2 = plt.figure(figsize=(5, 4))
ax2 = fig2.add_subplot()
x2 = np.arange(-2, 2, 0.1)
y1 = np.array([-y**2 for y in x2]) + 8
y2 = np.array([-y**2 for y in x2]) + 8
y3 = np.array([-y**2 for y in x2]) + 8
ax2.stackplot(x2, y1, y2, y3)
ax2.grid()
fig2.show()

fig3 = plt.figure(figsize=(6, 4))
ax3 = fig3.add_subplot()
x3 = np.arange(-np.pi, np.pi, 0.3)
ax3.stem(x3, np.cos(x3), '--r', '^g', ':', bottom=0.5)
ax3.grid()
fig3.show()

fig4 = plt.figure(figsize=(6, 4))
ax4 = fig4.add_subplot()
x = np.random.normal(0, 2, 500)
y = np.random.normal(0, 2, 500)
ax4.scatter(x, y, s=5, c='g', lw=0.1, marker='s', edgecolors='r')
ax4.grid()
fig4.show()

plt.show()
