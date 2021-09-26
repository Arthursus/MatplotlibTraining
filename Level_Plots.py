import numpy as np
import matplotlib.pyplot as plt

# x = np.arange(-2 * np.pi, 2 * np.pi, 0.2)
# y = np.arange(-2 * np.pi, 2 * np.pi, 0.2)
# xgrid, ygrid = np.meshgrid(x, y)
# zgrid = np.sin(xgrid) * np.sin(ygrid) / (xgrid * ygrid)

# fig = plt.figure(figsize=(7, 4))
# ax_3d = fig.add_subplot(projection='3d')

# ax_3d.contour(xgrid, ygrid, zgrid)  # 3D plot in the form of level lines
# ax_3d.contourf(xgrid, ygrid, zgrid)  # 3D plot in the form of level surfaces

fig, ax = plt.subplots(1, 2)
fig.set_size_inches(10, 5)

# c0 = ax[0].contour(xgrid, ygrid, zgrid, [-0.5, -0.2, 0, 0.2, 0.5, 0.7], colors=['g', 'b', 'r'])  # 2D plot in the form of level lines
# c1 = ax[1].contourf(xgrid, ygrid, zgrid, 15, cmap='Reds')  # 2D plot in the form of level surfaces
# c0.clabel(colors='k', fmt='%.2f')  # Analog of ax[0].clabel(c0)

x = np.random.rand(100) * 4 * np.pi - 2 * np.pi
y = np.random.rand(100) * 4 * np.pi - 2 * np.pi
z = np.sin(x) * np.sin(y) / (x * y)

c0 = ax[0].tricontour(x, y, z, cmap='inferno')  # Contour plotting with one-dimensional arrays
ax[1].tricontourf(x, y, z, 10)  # Surface plotting with one-dimensional arrays
c0.clabel(colors='k', fmt='%.2f')

plt.show()
