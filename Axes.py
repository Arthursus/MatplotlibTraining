import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullLocator, LinearLocator, MultipleLocator, IndexLocator, FixedLocator, LogLocator,\
    MaxNLocator

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot()
x = np.arange(-np.pi/2, np.pi, 0.1)
y = np.sin(x)
ax.plot(x, y)

# Set axes limits
ax.set_xlim(xmin=-3)
ax.set_ylim(ymax=2)

# The same
# ax0.set(xlim=(-5, 30), ylim=(-1, 6))

# If only one plot, we don't use ax.set... just
# plt.xlim(-1, 20)
# plt.ylim(-1, 6)

ax.minorticks_on()
ax.grid(which='major', lw=2)
ax.grid(which='minor')

ax.xaxis.set_minor_locator(NullLocator())

# LinearLocator sets fixed amount of marks
# ax.xaxis.set_major_locator(LinearLocator(5))

# MultipleLocator sets constant difference between marks
# ax.xaxis.set_major_locator(MultipleLocator(base=1))

# IndexLocator is as MultipleLocator plus sets start position
# ax.xaxis.set_major_locator(IndexLocator(base=0.5, offset=-0.43))

# FixedLocator sets marks in fixed positions
ax.xaxis.set_major_locator(FixedLocator([-2, -1, 1, 2, 3]))

# LogLocator is for logarithm divisions
# ax.xaxis.set_major_locator(LogLocator(base=2))

# MaxNLocator divide on specified maximum amount of marks
ax.yaxis.set_major_locator(MaxNLocator(10))

plt.show()
