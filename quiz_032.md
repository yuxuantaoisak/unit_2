## Solution ##

```.py

import matplotlib.pyplot as plt
import matplotlib
from matplotlib.gridspec import GridSpec

from lib_api import get_sensors

plt.style.use('ggplot')
matplotlib.use('MacOSX')

ids = [4, 5]
sensor = get_sensors(ids)

dif = []
for i in range(len(sensor[4])):
    x = (- sensor[5][i] - sensor[4][i]) / 2
    dif.append(x)


fig = plt.figure(figsize=(10, 5))
grid = GridSpec(4, 4, fig)
plt.subplots_adjust(hspace=0.5)

box_1 = fig.add_subplot(grid[1, 0])
plt.plot(sensor[4], color="black")
plt.title("sensor id=4")

box_2 = fig.add_subplot(grid[1, 3])
plt.plot(sensor[5], color="black")
plt.title("sensor id=5")

box_3 = fig.add_subplot(grid[0:3, 1:3])
plt.plot(dif, color="red")
plt.title("sensor id 4 - sensor id 5")
plt.show()


```

## Proof of work ##

<img width="1470" alt="Screenshot 2023-12-05 at 15 02 16" src="https://github.com/yuxuantaoisak/unit_2/assets/144768397/c588d355-2a8d-4e18-b0f0-26e172b8d1ed">
