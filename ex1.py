import numpy as np
import matplotlib
import matplotlib.pyplot as plt

print(matplotlib.get_backend())

y = np.arange(0, 5, 1)
x = np.array([a*a for a in y])

y1 = [0, 1, 2, 3]
x1 = [i+1 for i in y1]

lines = plt.plot(x, y, '--', x1, y1, ':', color=(0, 0, 0, 0.5))
print(lines)
plt.grid()
plt.show()

lines = plt.plot(x, y, 'r--', x1, y1, ':g', marker='o', markerfacecolor='w')
plt.setp(lines[1], linestyle='-.', marker='s', markerfacecolor='b', linewidth=3)
plt.grid()
plt.show()

x = np.arange(-2*np.pi, 2*np.pi, 0.1)
y = np.cos(x)
plt.plot(x, y)
plt.fill_between(x, y, where=y < 0, color='r', alpha=0.4)
plt.fill_between(x, y, where=y > 0, color='g', alpha=0.8)
plt.grid()
plt.show()
