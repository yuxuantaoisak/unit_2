## Solution ##

```.py

def case_1(my_dict, msg):

    for i in range(len(msg)):
        letter = msg[i]
        if letter in my_dict:
            my_dict[letter] += 1
    return my_dict


a = {'w': 0, 'l': 0, 'c': 0}
b = "hello world"

c = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
d = "Why did I choose CS?"

print(case_1(a, b))
print(case_1(c, d))


```

## Proof of work ##

<img width="1470" alt="Screenshot 2023-11-28 at 23 07 24" src="https://github.com/yuxuantaoisak/unit_2/assets/144768397/4c05fd4a-cae7-4c77-89d6-62e4d8788663">


## Part B ##

2^6 = 64 colors
