import numpy as np
import matplotlib.pyplot as plt

arr = np.arange(-2*np.pi, 2* np.pi)
y = np.sin(arr)

plt.figure()
plt.plot(arr, y)
plt.show()
