import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi, 1500)

bajo = np.sin(2*t)
melodia = 0.5*np.sin(10*t)
bateria = np.sign(np.sin(20*t))

mezcla = bajo + melodia + bateria

# segmento
segment = slice(400, 600)

plt.figure(figsize=(12,8))

plt.subplot(4,1,1)
plt.plot(bajo)
plt.title("Bajo")

plt.subplot(4,1,2)
plt.plot(melodia)
plt.title("Melodía")

plt.subplot(4,1,3)
plt.plot(bateria)
plt.title("Batería")

plt.subplot(4,1,4)
plt.plot(mezcla)
plt.plot(np.arange(segment.start, segment.stop), mezcla[segment], linewidth=3)
plt.title("Mezcla (con segmento resaltado)")

plt.tight_layout()
plt.show()
