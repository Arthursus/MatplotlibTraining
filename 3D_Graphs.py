import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(7, 4))
# ax_3d = Axes3D(fig) # deprecated
ax_3d = fig.add_subplot(projection='3d')

# x = np.linspace(0, 10, 50)
# z = np.cos(x)
# ax_3d.plot(x, x, z)

x = np.arange(-2 * np.pi, 2 * np.pi, 0.2)
y = np.arange(-2 * np.pi, 2 * np.pi, 0.2)
xgrid, ygrid = np.meshgrid(x, y)
zgrid = np.sin(xgrid) * np.sin(ygrid) / (xgrid * ygrid)

# ax_3d.plot_wireframe(xgrid, ygrid, zgrid)
# ax_3d.plot_surface(xgrid, ygrid, zgrid, rstride=1, cstride=5, cmap='plasma')
ax_3d.scatter(xgrid, ygrid, zgrid, s=1, color='g')

ax_3d.set_xlabel('x')
ax_3d.set_ylabel('y')
ax_3d.set_zlabel('z')

plt.show()
