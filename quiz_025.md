## Solution ##

```.py

import numpy as np
import matplotlib.pyplot as plt

#step 1: read data.csv

data = []

with open("quiz_025_data.csv", "r") as f:
    titles = f.readline()
    values = f.readlines()

print(titles)
print(values)

x = []
t = 0  #time in hours


for v in values:
    s1, s2, s3, s4, s5, s6, s7, s8, s9, s10 = v.strip().split(',')
    data.append([int(s1), int(s2), int(s3), int(s4), int(s5), int(s6), int(s7), int(s8), int(s9), int(s10)])
    x.append(t)
    t += 1

print(data)

#step 2: calculate descriptive stats

mean = []
std = []  #standard deviation
min_t = []
max_t = []

for d in data:
    mean.append(np.mean(d))
    std.append(np.std(d))
    min_t.append(np.min(d))
    max_t.append(np.max(d))


print(mean)
print(std)

#visualize the stats (errorbar graph)



plt.errorbar(x, mean, std, fmt="o", color="#023047")

plt.xlabel("Time (hours)")
plt.ylabel("Temperature (C)")
plt.show()

```


## Proof of work ##

![Screenshot 2023-11-28 at 21 51 27](https://github.com/yuxuantaoisak/unit_2/assets/144768397/d08f3600-d520-4a6f-9238-35c6cab975a9)

## Part B ##

red = 250 = FA

green = 100 = 64

blue = 10 = 0A

RGB color = #FA640A


