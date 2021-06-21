#use the python's built in function 'replace'(which has time
#complexity of O(n)) which inturn changes the total time complexity
# to O(n)^2

def url(string, length):
    for i in range(length):
        if string[i] == ' ':
            url_string = string.replace(' ','%20')
    return(url_string)