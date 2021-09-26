import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, ArtistAnimation

# plt.ion()

fig, ax = plt.subplots()

x = np.arange(-2*np.pi, 2*np.pi, 0.1)
y = np.cos(x)
line, = ax.plot(x, y)

# for delay in np.arange(-2*np.pi, 2*np.pi, 0.1):
#     y = np.cos(x + delay)
#
#     line.set_ydata(y)
#
#     plt.draw()
#     plt.gcf().canvas.flush_events()
#
#     time.sleep(0.02)


def update_cos(frame, line0, x0):
    # frame - parameter changing from frame to frame
    # in this case this is an initial phase (degree)
    # line0 - link to Line2D object
    line0.set_ydata(np.cos(x0 + frame))
    return [line0]


phasa = np.arange(0, 4*np.pi, 0.1)

animation = FuncAnimation(
    fig,                # Figure displaying animation
    func=update_cos,    # Updating current frame function
    frames=phasa,       # Parameter changing from frame to frame
    fargs=(line, x),    # Additional parameters for update_cos function
    interval=30,        # Delay between frames (ms)
    blit=True,          # Double buffering
    repeat=False        # Cycling of animation
)

# plt.ioff()
plt.show()
