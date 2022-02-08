pay_load = {"payload": ["a quick brown fox jumped over the lazy dog",
                        "brown fox jumped",
                        "the lazy dog",
                        "brown fox jumped over"]}
y = {}

for item in pay_load.values():
    for i in item:
        print(i)
        x = i.split(' ')
        print(x)
        for i in range(0, len(x), 1):
            if x[i] in y.keys():
                y[x[i]] = y[x[i]] + 1
            else:
                y[x[i]] = 1

print(y)
