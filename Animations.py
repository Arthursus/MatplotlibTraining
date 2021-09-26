import time
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2*np.pi, 2*np.pi, 0.1)

plt.ion()
for delay in np.arange(-2*np.pi, 2*np.pi, 0.1):
    y = np.cos(x + delay)

    plt.clf()
    plt.plot(x, y)

    plt.draw()
    plt.gcf().canvas.flush_events()

    time.sleep(0.02)

plt.ioff()
plt.show()
