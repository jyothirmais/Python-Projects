def reverse_string(string2):
    if ' ' in string2:
        string1 = string2.split(" ")
        x = len(string1)
        list1 = []
        for i in range(0, x, 1):
            list1.append(string1[x - 1 - i])
        print(' '.join(list1))
    else:
        x = len(string2)
        list1 = []
        for i in range(0, x, 1):
            list1.append(string2[x - 1 - i])
        print(''.join(list1))


reverse_string()
