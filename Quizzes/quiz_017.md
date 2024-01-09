## Solution ##

```.py
def get_l3tt3r(msg):
    num = len(msg)
    letters = {'i': 1, 'e': 3, 'o': 0, 'a': 4, ' ': "_"}
    output = ''

    for x in range(num):
        if msg[x] in letters:
            output += str(letters[msg[x]])
        else:
            output += msg[x]

    return output


case_1 = str(input("Please enter the message: "))
print(get_l3tt3r(case_1))
```


## Proof of work ##

<img width="985" alt="Screenshot 2023-11-22 at 21 59 33" src="https://github.com/yuxuantaoisak/unit_2/assets/144768397/8aa4911f-0ece-4db0-ba2f-b69f4d899968">

## Part B ##

![1284](https://github.com/yuxuantaoisak/unit_2/assets/144768397/0a02ca14-14ea-4ade-8e17-8e247ec1f443)

