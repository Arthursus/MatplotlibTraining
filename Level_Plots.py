import numpy as np
import matplotlib.pyplot as plt

# fig = plt.figure(figsize=(7, 4))
# ax_3d = fig.add_subplot(projection='3d')

fig, ax = plt.subplots(1, 2)
fig.set_size_inches(10, 5)

x = np.arange(-2 * np.pi, 2 * np.pi, 0.2)
y = np.arange(-2 * np.pi, 2 * np.pi, 0.2)
xgrid, ygrid = np.meshgrid(x, y)
zgrid = np.sin(xgrid) * np.sin(ygrid) / (xgrid * ygrid)

# ax_3d.contour(xgrid, ygrid, zgrid)  # 3D plot in the form of level lines
# ax_3d.contourf(xgrid, ygrid, zgrid)  # 3D plot in the form of level surfaces

c0 = ax[0].contour(xgrid, ygrid, zgrid, [-0.5, -0.2, 0, 0.2, 0.5, 0.7], colors=['g', 'b', 'r'])  # 2D plot in the form of level lines
c1 = ax[1].contourf(xgrid, ygrid, zgrid, 15, cmap='Reds')  # 2D plot in the form of level surfaces

c0.clabel(colors='k', fmt='%.2f')  # Analog of ax[0].clabel(c0)

plt.show()
