# one way check: check if two words are one way or zero edits way from being the same

def oneWay(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    counter = 0

    
    for i in s2:
        if i in s1:
            counter += 1

    if counter == len(s2) or counter +1 == len(s2):
        return True
    
    return False

print(oneWay('pale','ple'))
print(oneWay('pale','bake'))
    
    
