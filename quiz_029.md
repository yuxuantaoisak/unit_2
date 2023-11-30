## Solution ##

```.py

def sort_dict(case):
    case = dict(case)
    keys = []
    values = []
    new_dict = {}

    for k, v in case.items():
        keys.append(k)
        values.append(v)

    keys_sorted = [keys[0]]
    values_sorted = [values[0]]

    for i in range(1, len(values)):
        j = 0
        while j < len(values_sorted) and values[i] > values_sorted[j]:
            j += 1
        keys_sorted.insert(j, keys[i])
        values_sorted.insert(j, values[i])

    for k, v in zip(keys_sorted, values_sorted):
        new_dict[k] = v

    return new_dict


example = {'apple': 5, 'banana': 2, 'orange': 8, 'grape': 1}
example_2 = {'python': 3, 'java': 8, 'c++': 5, 'javascript': 2}
a = sort_dict(example)
b = sort_dict(example_2)
print(a)
print(b)

```

## Proof of work ##

<img width="441" alt="Screenshot 2023-11-23 at 9 01 53" src="https://github.com/yuxuantaoisak/unit_2/assets/144768397/f1a8d4be-31da-4336-bdcc-d4a0c1934d81">

## Part B ##

### Code ###

```.py

import matplotlib.pyplot as plt
import math

x = []
y = []


for i in range(1000):
    new_x = i / 1000
    new_y = math.sin(2*math.pi*new_x)
    x.append(new_x)
    y.append(new_y)

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("$sin(2*pi*x)$")
plt.title("$y=sin(2*pi*x)$")
plt.show()

```

<img width="1470" alt="Screenshot 2023-11-30 at 9 41 10" src="https://github.com/yuxuantaoisak/unit_2/assets/144768397/ee1e7440-6e10-40f9-b618-09272ca8153d">
