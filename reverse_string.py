def reverse_string(string1):
    x = len(string1)
    list1 = []
    for i in range(0, x, 1):
        list1.append(string1[x - 1 - i])
    print(''.join(list1))


reverse_string("euqeSNFKSJKSDJ")
