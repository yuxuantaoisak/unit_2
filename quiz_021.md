## Solution ##

```.py

import random
import matplotlib.pyplot as plt

random.seed(1234)


def produce(n: int, m: int, s: int):

    x = []
    y = []
    n = 5
    m = 3
    s = 2
    for i in range(n):
        x_rnd = random.randint(1, 100)
        y_rnd = x_rnd**(0.5*((m/s)**2))
        # should be positive 0.5 if the previous one is correct
        y.append(y_rnd)
        x.append(x_rnd)
    return x, y


data_y, data_x = produce(n=5, m=3, s=2)

fig = plt.figure(figsize=(9, 7))


plt.plot(data_x, data_y, color="r", marker="o", linewidth=2)


plt.xlabel("x", fontsize=18)
plt.ylabel("$y=x^{1/2(m/s)^2}$", fontsize=18)
plt.show()

```

## Proof of work ##

<img width="894" alt="Screenshot 2023-11-22 at 22 44 33" src="https://github.com/yuxuantaoisak/unit_2/assets/144768397/f945ad59-0889-439c-9675-e16cf8e822e5">

## Part B ##

### Truth table ###

| A | B | A XOR B | A(A XOR B) |
|---|---|---------|------------|
| 0 | 0 | 0       | 0          |
| 0 | 1 | 1       | 0          |
| 1 | 0 | 1       | 1          |
| 1 | 1 | 0       | 0          |
