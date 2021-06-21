def isUniqueOne(string):
    if len(string) > 128:
        return(False)
    char_set = [False] * 128
    for i in string:
        value = ord(i)    # this will give the ascii value of i
        if char_set[value]:
            return(False)
        char_set[value] = True
    return True

print(isUniqueOne('Hello'))