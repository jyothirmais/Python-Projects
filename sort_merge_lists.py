list1 = [3, 4, 9]
list2 = [1, 2, 7]


def sorted_list(list1, list2):
    list3 = list1 + list2
    for i in range(0, len(list3), 1):
        if i < len(list3) - 1:
            x = list3[i]
            y = list3.index(min(list3[i + 1:]))
            z = list3[y]
            if x < z:
                list3[i] = x
                list3[y] = z
            else:
                list3[i] = z
                list3[y] = x
    return print(list3)


sorted_list(list1, list2)
