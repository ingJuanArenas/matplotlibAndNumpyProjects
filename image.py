import numpy as np
import matplotlib.pyplot as plt


matrix = np.zeros((20,20,3))

matrix[5:12, 5:12] = [1,0,0]
matrix[15:22, 15:22] = [0,0,1]
matrix[:, 10] = [0,1,0]
matrix[10, :] = [0,1,0]
matrix[10, 10] = [1,1,1]

plt.imshow(matrix, cmap='gray')
plt.show()