import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7, 4))
ax_3d = fig.add_subplot(projection='3d')

x = np.arange(-2 * np.pi, 2 * np.pi, 0.2)
y = np.arange(-2 * np.pi, 2 * np.pi, 0.2)
xgrid, ygrid = np.meshgrid(x, y)
zgrid = np.sin(xgrid) * np.sin(ygrid) / (xgrid * ygrid)

# ax_3d.contour(xgrid, ygrid, zgrid)  # 3D plot in the form of level lines
ax_3d.contourf(xgrid, ygrid, zgrid)  # 3D plot in the form of level surfaces

plt.show()
