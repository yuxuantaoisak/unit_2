## Solution ##


```.py

import matplotlib.pyplot as plt
from lib_api import get_sensors, smoothing

s1 = get_sensors([1])[1]
s2 = get_sensors([2])[2]

for i in range(len(s1)):
    s1[i] += 1

for i in range(len(s2)):
    s2[i] += 1

x = []
for i in range(len(s1)):
    x.append(s1[i] + s2[i])

a, b = smoothing(values=x)

fig = plt.figure(figsize=(10, 8))
plt.subplot(3, 1, 1)
plt.plot(s2, color="red")
plt.subplot(3, 1, 2)
plt.plot(s1, color="blue")
plt.subplot(3, 1, 3)
plt.plot(a, b, color="red")
plt.show()


```

## Proof of work ##

<img width="1461" alt="Screenshot 2023-12-05 at 22 53 26" src="https://github.com/yuxuantaoisak/unit_2/assets/144768397/4c012e06-e75d-499e-a2cb-bf6c8a96da38">


