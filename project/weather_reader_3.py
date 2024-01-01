import csv
import matplotlib.pyplot as plt
import numpy as np
from lib_api import smoothing

hum = []
time = []
hum_lin = []
time_lin = []

with open('weather.csv', mode='r') as f:
    csv_reader = csv.DictReader(f)
    for row in csv_reader:
        hum_2 = row['Humidity']
        hum_2 = float(hum_2)
        hum.append(hum_2)
        time.append(5 * len(hum))
        hum_lin.append(hum_2)
        time_lin.append(5 * len(hum))

m, b = np.polyfit(time_lin, hum_lin, 1)
hum_lin_model = [m * t + b for t in time_lin]


# Calculate smoothed values
smoothed_x, smoothed_y = smoothing(values=hum)

# Plotting

plt.plot(smoothed_x, smoothed_y, label='Original curve')
plt.plot(time_lin, hum_lin_model, label=f"Linear Model: f(t) = {m:.2f}t + {b:.2f}")
plt.title("Linear model for indoor humidity")
plt.xlabel("Time (minutes)")
plt.ylabel("%")
plt.xlim(0, 600)
plt.ylim(25, 35)
print(f"The linear model is f(t) = {m:.2f}t + {b:.2f}")
plt.legend()
plt.show()
