import numpy as np
import matplotlib.pyplot as plt



matrix = np.random.randint(10,40, (7,24))

plt.figure()
plt.imshow(matrix, cmap='hot')
plt.show()