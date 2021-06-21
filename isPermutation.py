# we can have two solution to thsi question 

def isPermOne(string1,string2):
    if len(string1) != len(string2):
        return(False)
    
    string1, string2 = sorted(string1), sorted(string2)
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            return(False)
    return(True)


def isPermTwo(string1, string2):
    if set(string1) == set(string2):
        return(True)