import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8, 6))
ax0 = fig.add_subplot()
ax0.plot(np.arange(1, 5, 0.25))

# Set axes limits
# ax0.set_xlim(xmin=-5)
# ax0.set_ylim(ymax=6)

# The same
# ax0.set(xlim=(-5, 30), ylim=(-1, 6))

# If only one plot, we don't use ax.set... just
plt.xlim(-1, 20)
plt.ylim(-1, 6)

plt.show()
