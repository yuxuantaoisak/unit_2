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
