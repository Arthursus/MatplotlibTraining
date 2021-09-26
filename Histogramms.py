import matplotlib.pyplot as plt
import numpy as np

y = np.random.normal(0, 2, 500)
x = np.linspace(np.min(y), np.max(y), 10)
bars = [len(y[np.bitwise_and(y >= x[i], y < x[i + 1])]) for i in range(len(x) - 1)]
values = x + np.append(np.diff(x), 0) / 2  # Bringing to fitting size of bars

fig1 = plt.figure(figsize=(6, 4))
ax = fig1.add_subplot()
ax.bar(values[:-1], bars)
fig1.show()

# ax.hist(y, 50)

fig2 = plt.figure(figsize=(6, 4))
ax = fig2.add_subplot()
ax.barh(values[:-1], bars)
fig2.show()

plt.show()
