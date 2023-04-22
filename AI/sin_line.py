import math

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2 * math.pi, 0.01)
y = np.sin(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sine Wave')
plt.show()
