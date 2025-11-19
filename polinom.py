import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10)
y= 2*x**2 + 3*x + 1


plt.figure()
plt.plot(x, y)
plt.show()

y= -3*x**3+x**2-x+5

plt.figure()
plt.plot(x, y)
plt.show()


y= np.sin(x) + 0.3* np.cos(3*x)
plt.figure()
plt.plot(x, y)
plt.show()