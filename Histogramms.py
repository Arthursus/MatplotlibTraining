import matplotlib.pyplot as plt
import numpy as np

# x = [f'H{i+1}' for i in range(10)]
# y = np.random.randint(-20, 20, len(x))

x = np.arange(10)
y1 = np.random.randint(3, 20, len(x))
y2 = np.random.randint(3, 20, len(x))

fig = plt.figure(figsize=(6, 4))
ax = fig.add_subplot()
# ax.bar(x, y, width=0.5, linewidth=2, edgecolor='r', yerr=2, bottom=10)
w = 0.3
ax.bar(x - w/2, y1, width=w)
ax.bar(x + w/2, y2, width=w)
ax.grid()

# y = np.random.normal(0, 2, 500)
# x = np.linspace(np.min(y), np.max(y), 10)
# bars = [len(y[np.bitwise_and(y >= x[i], y < x[i + 1])]) for i in range(len(x) - 1)]
# values = x + np.append(np.diff(x), 0) / 2  # Bringing to fitting size of bars

# fig1 = plt.figure(figsize=(6, 4))
# ax = fig1.add_subplot()
# ax.bar(values[:-1], bars)
# fig1.show()

# ax.hist(y, 50)

# fig2 = plt.figure(figsize=(6, 4))
# ax = fig2.add_subplot()
# ax.barh(values[:-1], bars)
# fig2.show()

plt.show()
