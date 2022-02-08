def anagram(string1, string2):
    if len(string1) == len(string2):
        for i in range(0, len(string1), 1):
            x = string1[i] in string2
            if x is True:
                if i == len(string1) - 1:
                    return True
            else:
                return False
                break
    else:
        return False


print(anagram("new yrxk times",  "mkeys write"))
