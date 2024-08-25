import matplotlib.pyplot as plt
import numpy as np

center = (0.5, 0.5)
radius = 0.4
theta = np.linspace(0, (3 / 4) * np.pi, 200)
x_circle = center[0] + radius * np.cos(theta)
y_circle = center[1] + radius * np.sin(theta)
plt.plot(x_circle, y_circle, color='red', label='Half Circle')
# plt.xlim(1)
# plt.ylim(1)
plt.show()