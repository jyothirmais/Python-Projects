import math


def reverse_string(string2):
    string1 = string2.split(" ")
    x = len(string1)
    for i in range(0, x, 1):
        if i == math.floor(x / 2):
            m = string1[i]
            z = string1[x - 1 - i]
            string1[i] = m
            string1[x - 1 - i] = z
            break
        else:
            y = string1[i]
            z = string1[x - 1 - i]
            string1[i] = z
            string1[x - 1 - i] = y
            continue

    print(' '.join(string1))


reverse_string("CAKE BAKE MAKE LAKE TAKE WAKE SAKE RAKE BJHKJK HBJHVG")
