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


fig = plt.figure(figsize=(10, 8))
plt.subplot(3, 1, 1)
plt.plot(s2, color="red")
plt.subplot(3, 1, 2)
plt.plot(s1, color="blue")
plt.subplot(3, 1, 3)
plt.plot(x, color="red")
plt.show()


```

## Proof of work ##

![Screenshot 2023-12-04 at 23 56 34](https://github.com/yuxuantaoisak/unit_2/assets/144768397/f3f5d44f-634c-4979-ab56-5e56d6fcbc04)

