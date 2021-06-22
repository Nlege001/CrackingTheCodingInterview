# 4. palindrome permutation
# a palindrome is a word or a phrase that has the same meaning when its read forward and backward
# for a word or a phrase to be a palindrome, it must have at one letter that appears once(odd number of times) and the other must appear in even counts

def palindromePerm(s):
    s = s.replace(' ','') # this is because casing and spacing doesn't matter 
    
    s = s.lower()
    char_list = {}
    odd_counter = 0

    for i in s:
        if i in char_list:
            char_list[i] +=1
        else:
            char_list[i] = 1
    for i,j in char_list.items():
        if j %2 != 0 and odd_counter == 0:
            odd_counter +=1
        if j %2 != 0 and odd_counter != 0:
            return False
    return True
    



print(palindromePerm('ayakk'))



