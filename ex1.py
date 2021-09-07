import numpy as np
import matplotlib
import matplotlib.pyplot as plt

print(matplotlib.get_backend())

y = np.arange(0, 5, 1)
x = np.array([a*a for a in y])

# y1 = [0, 1, 2, 3]
# x1 = [i+1 for i in y1]

plt.plot(x, y, '--')
plt.grid()
plt.show()
