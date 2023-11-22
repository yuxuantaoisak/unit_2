## Solution ##

```.py

import numpy as np
import matplotlib.pyplot as plt

data = {
    'x': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
    'y': [24, 1, 2, 25, 26, 21, 23, 34, 49, 2, 19, 32, 7, 17, 36, 7, 45, 28, 40, 46]
}

data['title'] = "quiz_data_science"


values_x = data['x']
values_y = data['y']

x = []
y = []

for i in data:
    for x_value in data['x']:
        x.append(x_value)
    for y_value in data['y']:
        y.append(y_value)

plt.plot(x, y)
plt.title(data['title'])
plt.xlabel('x')
plt.ylabel('y')
plt.show()

```

## Proof of work ##

<img width="588" alt="Screenshot 2023-11-23 at 8 48 44" src="https://github.com/yuxuantaoisak/unit_2/assets/144768397/e5c0d24d-1f29-4332-9b41-fc1324b0cf87">

## Part B ##
