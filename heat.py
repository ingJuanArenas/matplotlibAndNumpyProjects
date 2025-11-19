import numpy as np
import matplotlib.pyplot as plt



matrix = np.random.randint(10,40, (7,24))

plt.figure()
plt.imshow(matrix)
plt.show()



matrix2= np.zeros((20,20,))
matrix2[:,:10] = 50
matrix2[:,10:20] = 100

plt.imshow(matrix2)
plt.show()