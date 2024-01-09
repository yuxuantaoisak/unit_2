## solution ##

```.py

import random


def produce(n, m, s):
    out = ""
    random.seed(1234)
    x = []
    y = []
    for i in range(n):
        x_rnd = random.randint(1, 100)
        y_rnd = x_rnd**(0.5*((m/s)**2))
        y.append(y_rnd)
        x.append(x_rnd)
        out += f"|   {str(x_rnd).ljust(5)}   |   {y_rnd:.2f}\t   |\n"
    return out


sample = produce(n=5, m=3, s=2)
print(sample)

```

## Proof of work ##

<img width="238" alt="Screenshot 2023-11-22 at 22 37 46" src="https://github.com/yuxuantaoisak/unit_2/assets/144768397/da910bbd-a725-4be2-9977-89efdd2e1a84">

## Part B ##

A(A+B) = A

A = 0, B = 0:

0(0+0) = 0 = A


A = 0, B = 1:

0(0+1) = 0 = A


A = 1, B = 0:

1(1+0) = 1 = A


A = 1, B = 1:

1(1+1) = 1 = A


Thus, A(A+B) is always A.
