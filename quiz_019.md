## Solution ##

```.py

def get_truth():
    a = 1
    b = 1
    c = 1
    out = "| A | B | C | AB + not B + not CB |\n"

    for x in range(8):
        c = not c

        if x % 2 == 0:
            b = not b

        if x % 4 == 0:
            a = not a

        result = (a and b) or (not b) or (not (c and b))

        out += f"| {int(a)} | {int(b)} | {int(c)} |          {int(result)}          |\n"
    return out


table = get_truth()
print(table)
```

## Proof of work ##

<img width="313" alt="Screenshot 2023-11-22 at 22 34 48" src="https://github.com/yuxuantaoisak/unit_2/assets/144768397/565b12f2-b49f-403a-b68f-b9e65de61172">

## Part B ##
