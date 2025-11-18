import numpy as np
import matplotlib.pyplot as plt

mins= np.arange(0,90)
goles = np.zeros(90)
goles_minuto = np.random.choice(mins, size=2, replace=False)
goles[goles_minuto] += 1

tiros = np.random.randint(0,3,90)
posesion = 50 + 10*np.sin(mins/10) + np.random.normal(0, 5, 90)
posesion = np.clip(posesion, 30, 70)

# --- subplots ---
plt.figure(figsize=(12,8))

plt.subplot(3,1,1)
plt.plot(mins, goles)
plt.title("Goles por minuto")

plt.subplot(3,1,2)
plt.plot(mins, tiros)
plt.title("Tiros por minuto")

plt.subplot(3,1,3)
plt.plot(mins, posesion)
plt.title("Posesión (%)")

plt.tight_layout()
plt.show()