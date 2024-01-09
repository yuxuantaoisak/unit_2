## Solution ##

```.py

import matplotlib
import matplotlib.pyplot as plt
import math

para_1_x = []
para_1_y = []
para_2_x = []
para_2_y = []
t = -2

while t < 2:
    para_1_x.append(t)
    para_1_y.append(t**2)
    para_2_x.append(t)
    para_2_y.append(-(t**2))
    t += 0.04
    if t == 4:
        break

plt.plot(para_1_x, para_1_y, label="parabola 1 (x axis)")
plt.plot(para_2_x, para_2_y, label="parabola 2 (x axis)")
plt.plot(para_1_y, para_1_x, label="parabola 3 (y axis)")
plt.plot(para_2_y, para_2_x, label="parabola 4 (y axis)")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.legend()
plt.show()


```


## Proof of work ##

<img width="1161" alt="Screenshot 2023-12-16 at 11 01 47" src="https://github.com/yuxuantaoisak/unit_2/assets/144768397/16d947da-8ec8-4637-8f46-e6d03ba1eecd">




