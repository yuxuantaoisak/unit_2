## Solution ##

```
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from lib_api import get_sensors, smoothing

s = get_sensors([2])
print(s)
fig = plt.figure(figsize=(10, 8))
x, y = smoothing(values=s[2])

print(x)
x_new = []
y_new = []

for i in range(1, len(x)):
    if 200 < x[i] < 400:
        x_new.append(x[i])
        y_new.append(y[i])

plt.plot(x_new, y_new, color="black")
plt.title("sensor 2")

m, b = np.polyfit(x_new, y_new, 1)
x_lin = []
y_lin = []
for i in range(200, 400):
    x_lin.append(i)
    y_lin.append(m*i + b)

print(f"The linear model is f(t) = {m:.2f}t + {b:.2f}")
plt.plot(x_lin, y_lin, color="red")
plt.show()


```.py


