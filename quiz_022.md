## Solution ##

```.py

from matplotlib import pyplot as plt


def produce(x: int, y: int):
    x_list = []
    y_list = []
    for i in range(-10, 11):
        x = i
        y = 2*((x+5)**2)
        x_list.append(x)
        y_list.append(y)
    return x_list, y_list


data_x, data_y = produce(x=-10, y=50)
plt.plot(data_x, data_y)
plt.xlabel("x")
plt.ylabel("$f(x)=2(x+5)^2$")
plt.show()

```

## Proof of work ##

<img width="626" alt="Screenshot 2023-11-22 at 22 50 22" src="https://github.com/yuxuantaoisak/unit_2/assets/144768397/cde3c7c0-ee80-4862-ae8c-9941e34ff2ba">

## Part B ##
