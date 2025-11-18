import numpy as np
import matplotlib.pyplot as plt

img = np.zeros((200, 200, 3))

# cuadro rojo
img[20:80, 20:80] = [1, 0, 0]

# cuadro azul
img[120:180, 120:180] = [0, 0, 1]

# gradiente vertical
for i in range(200):
    img[:, i, 1] = i/200  # verde

plt.imshow(img)
plt.axis('off')
plt.show()
