## Solution ##

```.py


import matplotlib
import matplotlib.pyplot as plt

para_1_x = []
para_1_y = []
para_2_x = []
para_2_y = []

t = -6
m = 6
while t < 0:
    para_1_x.append(t)
    para_1_y.append((t+2)**2)
    para_2_x.append(m)
    para_2_y.append((m-2)**2)
    t += 0.04
    m -= 0.04
    if t == 0 and m == 0:
        break

neg_1 = []
neg_2 = []

for i in range(len(para_1_y)):
    neg_1.append(para_1_y[i]*-1)
    neg_2.append(para_2_y[i]*-1)

plt.plot(para_1_x, para_1_y, label="parabola 1")
plt.plot(para_2_x, para_2_y, label="parabola 2")
plt.plot(para_1_x, neg_1, label="parabola 3")
plt.plot(para_2_x, neg_2, label="parabola 4")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.legend()
plt.show()



```

## Proof of work ##

<img width="1267" alt="Screenshot 2023-12-16 at 10 59 13" src="https://github.com/yuxuantaoisak/unit_2/assets/144768397/3f8382a6-b559-46ec-a713-74b38bb28b76">


