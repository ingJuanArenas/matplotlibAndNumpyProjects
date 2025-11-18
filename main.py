import numpy as np
import matplotlib.pyplot as plt 

days = np.arange(1,31)  # days from 1 to 30
temperature = np.random.randint(18,32,30)
humidity = np.random.randint(1, 100, 30)
pressure = np.random.randint(1000, 1500, 30)

## stadistics

max_temp = temperature.max()
min_temp= temperature.min()
mean_temp = temperature.mean()
max_hum = humidity.max()
min_hum = humidity.min()
mean_hum = humidity.mean()
max_pres = pressure.max()
min_pres = pressure.min()
mean_pres = pressure.mean()

## NOW, PRINT ALL DE DATA IN ONE STEP
print("Temperature: ", temperature)
print("Humidity: ", humidity)
print("Pressure: ", pressure)
print("Max Temperature: ", max_temp)
print("Min Temperature: ", min_temp)
print("Mean Temperature: ", mean_temp)
print("Max Humidity: ", max_hum)
print("Min Humidity: ", min_hum)
print("Mean Humidity: ", mean_hum)
print("Max Pressure: ", max_pres)
print("Min Pressure: ", min_pres)
print("Mean Pressure: ", mean_pres)


plt.figure(figsize=(12,4))


plt.subplot(2,2,1)
plt.plot(days,temperature)
plt.title("Temperature in 1 month")
plt.xlabel("days")
plt.ylabel("pressure")


plt.subplot(2,2,2)
plt.plot(days, humidity)
plt.title("Humidity in 1 month")
plt.xlabel("days")
plt.ylabel("humity")


plt.subplot(2,2,3)
plt.plot(days, temperature,humidity)
plt.title("Temperature vs humidity")
plt.xlabel("days")
plt.legend("Temperature", "Humidity")


plt.subplot(2,2,4)
plt.hist(temperature, bins=7, density=True, alpha=0.6, color='b')
plt.title('Temperature Distribution')


plt.tight_layout()
plt.show()
