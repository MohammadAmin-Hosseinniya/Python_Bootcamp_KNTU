import numpy as np
import matplotlib.pyplot as plt

numbers = np.linspace(0, 2*np.pi, 360)
y = np.sin(numbers)

plt.plot(numbers, y)
plt.show()