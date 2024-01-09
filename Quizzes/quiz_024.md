## Solution ##

```.py

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')

h = [57.0, 56.0, 57.0, 56.0, 55.0, 55.0, 54.0, 54.0, 54.0,
     53.0, 53.0, 54.0, 53.0, 53.0, 52.0, 52.0, 51.0, 51.0,
     51.0, 50.0, 50.0, 49.0, 50.0, 49.0, 49.0, 48.0, 49.0,
     49.0, 48.0, 48.0, 48.0, 49.0]
t = []
time = 0
for i in range(0, len(h)):
    t.append(time)
    time += 10

plt.scatter(t, h, color="r")
plt.xlabel("Time(minutes)")
plt.ylabel("Humidity(%)")
plt.title("The humidity in ASAMA 22")

m, b = np.polyfit(t, h, 1)
print(f"The linear model is f(t) = {m:.2f}t + {b:.2f}")

time_model = []
hum_model = []
for i in range(0, 300, 5):
    time_model.append(i)
    hum_model.append(m*i + b)

plt.plot(time_model, hum_model, color="black")
plt.text(15, 14, f"f(x) = {m:.2f} + {b:.2f}", fontsize=20)
plt.show()

```

## Proof of work ##

<img width="593" alt="Screenshot 2023-11-25 at 13 56 57" src="https://github.com/yuxuantaoisak/unit_2/assets/144768397/9b280e59-baaf-4d02-888a-289380688013">

<img width="342" alt="Screenshot 2023-11-25 at 14 40 13" src="https://github.com/yuxuantaoisak/unit_2/assets/144768397/503f0a28-a092-474b-a301-695d64671749">

## Part B ##

e6e627

e6 = 14 * 16¹ + 6 * 16⁰ = 230

27 = 2 * 16¹ + 7 * 16⁰ = 39

rgb color = (230, 230, 39)
