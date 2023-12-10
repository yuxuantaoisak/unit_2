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

plt.plot(para_1_x, para_1_y)
plt.plot(para_2_x, para_2_y)
plt.plot(para_1_y, para_1_x)
plt.plot(para_2_y, para_2_x)
plt.show()


```


## Proof of work ##

<img width="1331" alt="Screenshot 2023-12-10 at 23 22 06" src="https://github.com/yuxuantaoisak/unit_2/assets/144768397/e60492a0-3020-4af4-8e49-7af307e9111e">


