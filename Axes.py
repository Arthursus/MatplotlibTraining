import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8, 6))
ax0 = fig.add_subplot()
ax0.plot(np.arange(1, 5, 0.25))
ax0.set(xlim=(-5, 30), ylim=(-1, 6))
# The same
# ax0.set_xlim=(-5, 30)
# ax0.set_ylim=(-1, 6)

plt.show()
