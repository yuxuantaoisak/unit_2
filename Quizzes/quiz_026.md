## Solution ##

```.py

import numpy as np
import matplotlib.pyplot as plt

data = {'x': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
        'y': [24, 1, 2, 25, 26, 21, 23, 34, 49, 2, 19, 32, 7, 17, 36, 7, 45, 28, 40, 46]
        }

data['title'] = "quiz_data_science"


values_x = data['x']
values_y = data['y']

plt.plot(values_x, values_y)
plt.title(data['title'])
plt.xlabel('x')
plt.ylabel('y')
plt.show()



```

## Proof of work ##

<img width="1379" alt="Screenshot 2023-12-05 at 23 18 32" src="https://github.com/yuxuantaoisak/unit_2/assets/144768397/c75df2c5-9979-4deb-ab5e-0887adfae938">



## Part B ##

red = 10 = 0A

green = 255 = FF

blue = 235 = EB

RGB = #0AFFEB
