## Solution ##

```.py

def get_truth():
    a = 1
    b = 1
    c = 1
    out = "| A | B | C |\n"

    for i in range(8):
        c = not c

        if i % 2 == 0:
            b = not b

        if i % 4 == 0:
            a = not a

        out += f"| {int(a)} | {int(b)} | {int(c)} |\n"
    return out


table = get_truth()
print(table)

```

## Proof of work ##

<img width="293" alt="Screenshot 2023-11-22 at 22 28 31" src="https://github.com/yuxuantaoisak/unit_2/assets/144768397/b4e692c0-4ddd-4651-8041-016ff8804b81">

## Part B ##

### Truth table ###

| S₁ | S₂ | S₃ | S₁S₂ | not S₁ | S₃(not S₁) | S₂+S₃(not S₁) | (S₂+S₃(not S₁))S₁ | S₁S₂+(S₂+S₃(not S₁))S₁ |
|----|----|----|------|--------|------------|---------------|-------------------|------------------------|
| 0  | 0  | 0  | 0    | 1      | 0          | 0             | 0                 | 0                      |
| 0  | 0  | 1  | 0    | 1      | 1          | 1             | 0                 | 0                      |
| 0  | 1  | 0  | 0    | 1      | 0          | 1             | 0                 | 0                      |
| 0  | 1  | 1  | 0    | 1      | 1          | 1             | 0                 | 0                      |
| 1  | 0  | 0  | 0    | 0      | 0          | 0             | 0                 | 0                      |
| 1  | 0  | 1  | 0    | 0      | 0          | 0             | 0                 | 0                      |
| 1  | 1  | 0  | 1    | 0      | 0          | 1             | 1                 | 1                      |
| 1  | 1  | 1  | 1    | 0      | 0          | 1             | 1                 | 1                      |

### Boolean circuit ###

![1285](https://github.com/yuxuantaoisak/unit_2/assets/144768397/effc1030-ac97-45e5-aa1c-7efa97b7006e)
