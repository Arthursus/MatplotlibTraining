import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = Image.open('packages.png')
data = np.random.randint(0, 256, (100, 100))

# fig = plt.figure(figsize=(4, 7))
# ax = fig.add_subplot()
# ax.imshow(img)

# The same
plt.imshow(img, origin='lower', aspect=0.4, alpha=0.7)
plt.show()

b = plt.imshow(data, cmap='plasma')
plt.colorbar(b)
plt.show()

plt.pcolormesh(data, edgecolors='black', shading='gouraud', cmap='gray')
plt.show()
