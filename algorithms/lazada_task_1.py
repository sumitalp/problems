import re
from itertools import count


def solution(s):
    s = re.sub('\d','',s)

    substr = longest_alphabet(s)
    if re.search(r'^(?=.*[a-z])(?=.*[A-Z]).+$', substr):
        return len(substr)

    return -1

def longest_alphabet(string):
    maxsubstr = string[0:0]
    
    for i in range(len(string)):
        for j in count(i + len(maxsubstr) + 1):
            substr = string[i:j]

            if len(substr) != (j - i):
                break

            if sorted(substr) == list(substr):
                maxsubstr = substr

    return maxsubstr



if __name__=='__main__':

    s1 = 'a0Ba'
    print(solution(s1))

    s2 = 'a0bb'
    print(solution(s2))
