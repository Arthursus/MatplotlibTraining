import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot()

x = np.arange(0, 10)

ax.step(x, x, '-go', x, np.cos(x), '--x', where='mid')

ax.grid()

plt.show()
