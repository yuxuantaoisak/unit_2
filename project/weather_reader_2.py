import csv
import matplotlib.pyplot as plt
import numpy as np
from lib_api import smoothing

temp = []
time = []
time_lin = []
temp_lin = []

with open('weather.csv', mode='r') as f:
    csv_reader = csv.DictReader(f)
    for row in csv_reader:
        temp_2 = float(row['Temperature'])
        temp.append(temp_2)
        time.append(5 * len(temp))
        time_lin.append(5 * len(temp))
        temp_lin.append(temp_2)  # Accumulate actual temperature values for linear model

# Fit a linear model after accumulating data
m, b = np.polyfit(time_lin, temp_lin, 1)

# Generate linear model predictions
temp_lin_model = [m * t + b for t in time_lin]

# Smoothing
smoothed_x, smoothed_y = smoothing(values=temp)

# Plotting
plt.plot(smoothed_x, smoothed_y, label="Original curve")
plt.plot(time_lin, temp_lin_model, label=f"Linear Model: f(t) = {m:.2f}t + {b:.2f}")
plt.title("Linear model for indoor temperature")
plt.xlabel("Time (minutes)")
plt.ylabel("Room temperature")
plt.legend()
plt.show()
