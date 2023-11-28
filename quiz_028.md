## Solution ##

```.py

def invert(test):
    inverted_dict = {}

    for k, v in test.items():
        inverted_dict[v] = k
    return inverted_dict


a = {'a': 1, 'b': 2, 'c': 3}
b = {'bob': 26, 'alice': 30, 'carl': 40}

print(invert(a))
print(invert(b))

```

## Proof of work ##

<img width="1470" alt="Screenshot 2023-11-28 at 23 24 01" src="https://github.com/yuxuantaoisak/unit_2/assets/144768397/43aeef9c-e57b-4d92-97cc-0367f96cb369">

## Part B ##

1011 = 11

1101 = 13

11 + 13 = 24

24(10) = 11000(2)
