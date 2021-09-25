import matplotlib.pyplot as plt
import numpy as np

fig1 = plt.figure(figsize=(6, 4))
ax1 = fig1.add_subplot()
y = np.random.normal(0, 2, 500)
ax1.hist(y, 50)
ax1.grid()
plt.show()
