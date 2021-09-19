import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot()
x = np.arange(-10 * np.pi, 10 * np.pi, 0.1)
y = np.sinc(x) * np.exp(-np.abs(x / 10))
# ax.semilogy(x, y)
# ax.loglog(x, y)
ax.plot(x, y)
ax.set_yscale('log', base=10, subs=[2, 9])
ax.set_xscale('symlog', linthresh=2, linscale=0.5)
ax.grid()

plt.show()
