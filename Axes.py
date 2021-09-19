import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullLocator, LinearLocator, MultipleLocator, IndexLocator, FixedLocator, LogLocator,\
    MaxNLocator
from matplotlib.ticker import NullFormatter, FormatStrFormatter, FuncFormatter, ScalarFormatter, FixedFormatter


def format0y(x, pos):
    return f"[{x}]" if x < 0 else f"({x})"


fig = plt.figure(figsize=(8, 6))
fig.set(facecolor='#eee')
ax = fig.add_subplot()
ax.set(facecolor='#AAFFAA')
x = np.arange(-np.pi/2, np.pi, 0.1)
y = np.sin(x) * 1e5
ax.plot(x, y)

plt.figtext(0.05, 0.6, "Text in a figure area", fontsize=18, c='r')
fig.suptitle("Figure title")
ax.set_xlabel("Ox")
ax.set_ylabel("Oy")
# plt.xlabel("Ox")
# plt.ylabel("Oy")
ax.text(-1, 1.0, "Arbitrary text in an axes area", bbox={'boxstyle': 'darrow', 'facecolor': '#AAAAFF'})
ax.annotate("Annotation", xy=(1.0, -0.4), xytext=(2.0, 0.9), arrowprops={'facecolor': 'gray', 'shrink': 0.1})

# Set axes limits
ax.set_xlim(xmin=-2)
# ax.set_ylim(ymax=1)

# The same
# ax0.set(xlim=(-5, 30), ylim=(-1, 6))

# If only one plot, we don't use ax.set... just
# plt.xlim(-1, 20)
# plt.ylim(-1, 6)

ax.minorticks_on()
ax.grid(which='major', lw=2)
ax.grid(which='minor', ls=':')

ax.xaxis.set_minor_locator(NullLocator())

# LinearLocator sets fixed amount of marks
# ax.xaxis.set_major_locator(LinearLocator(5))

# MultipleLocator sets constant difference between marks
# ax.xaxis.set_major_locator(MultipleLocator(base=1))

# IndexLocator is as MultipleLocator plus sets start position
# ax.xaxis.set_major_locator(IndexLocator(base=0.5, offset=-0.43))

# FixedLocator sets marks in fixed positions
ax.xaxis.set_major_locator(FixedLocator([-2, -1, 0, 1, 2, 3]))

# LogLocator is for logarithm divisions
# ax.xaxis.set_major_locator(LogLocator(base=2))

# MaxNLocator divide on specified maximum amount of marks
ax.yaxis.set_major_locator(MaxNLocator(10))

# Manage ticks

# ax.set_xticklabels([])
# ax.set_yticklabels([])

# ax.xaxis.set_major_formatter(NullFormatter())

# ax.yaxis.set_major_formatter(FormatStrFormatter("y = %.2f"))

# Format with reference function
# ax.yaxis.set_major_formatter(FuncFormatter(format0y))

# Redefine default ScalarFormatter
sf = ScalarFormatter()
sf.set_powerlimits((-4, 4))
ax.yaxis.set_major_formatter(sf)

# FixedFormatter is used with FixedLocator
ax.xaxis.set_major_formatter(FixedFormatter(['-II', '-I', 'O', 'I', 'II', 'III']))

plt.show()
