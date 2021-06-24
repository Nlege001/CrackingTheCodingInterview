# string compression

def stringCompression(string):
    compressed = []
    counter = 0

    for i in range(len(string)):  
        if i != 0 and string[i] != string[i - 1]:
            compressed.append(string[i - 1] + str(counter))
            counter = 0
        counter += 1
        print(i, compressed, counter)

    # add last repeated character
    if counter:
        compressed.append(string[-1] + str(counter)) # reverse index counting
    #print(i, compressed, counter)

    # returns original string if compressed string isn't smaller
    return min(string, "".join(compressed), key=len)


print(stringCompression('abbbaaaa'))
