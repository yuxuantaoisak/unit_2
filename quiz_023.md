## Solution ##

```.py

from matplotlib import pyplot as plt


def produce(x: int, y: int):
    x = []
    y = []

    for i in range(-10, 11):

        x_new = i

        if x_new < 0:
            y_new = -x_new
        elif x_new > 0:
            y_new = x_new
        else:
            y_new = 0
        x.append(x_new)
        y.append(y_new)
    return x, y


data_x, data_y = produce(x=-10, y=10)

plt.plot(data_x, data_y)
plt.xlabel("x", fontsize=18)
plt.ylabel("$f(x)=|x|$", fontsize=18)
plt.show()


```

## Proof of work ##

<img width="614" alt="Screenshot 2023-11-22 at 22 52 20" src="https://github.com/yuxuantaoisak/unit_2/assets/144768397/813b0067-0470-4454-b04c-a3ddeabbb661">

## Part B ##
