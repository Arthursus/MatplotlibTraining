import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import *

# l1 = Line2D([1, 2, 0], [1, 2, 3])

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot()

x = np.arange(-np.pi, np.pi, 0.1)
y1 = np.sin(x)
y2 = np.sinc(x)

cos = Line2D(x, np.cos(x))

rect = Rectangle((3, -0.5), 2.5, 0.5, facecolor='g')

line1, = ax.plot(x, y1, '--o', label='line 1')
line2, = ax.plot(x, y2, ':s', label='line 2')
# ax.legend((line2, line1), ['Линия 1', 'Линия 2'], bbox_to_anchor=(0.5, 0.7))
ax.legend([r'$f(x) = \sin(x)$', r'$f(x) = \frac{\sin(x)}{x}$'], loc='upper left', facecolor='#aaa', framealpha=0.5)
ax.grid()

ax.add_line(cos)
ax.set(xlim=(-2 * np.pi, 2 * np.pi), ylim=(-1, 1))
ax.add_patch(rect)

plt.show()
