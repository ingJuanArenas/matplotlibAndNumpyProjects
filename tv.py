import numpy as np
import matplotlib.pyplot as plt

matrix = np.random.randint(0,255,(200,300))

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i][j] = np.random.randint(0,255)


plt.imshow(matrix)
plt.show()