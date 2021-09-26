import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(7, 4))
# ax_3d = Axes3D(fig) # deprecated
ax_3d = fig.add_subplot(projection='3d')
plt.show()
