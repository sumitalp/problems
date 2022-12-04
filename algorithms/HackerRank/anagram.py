# HackerRank 'Anagram' problem

def count_char(s):
    ret = {}
    for c in s:
        if c not in ret:
            ret[c] = 1
        else:
            ret[c] += 1
    return ret
    
    
t = int(input())

for i in range(t):
    s = input()
    s1 = s[:len(s)//2]
    s2 = s[len(s)//2:]
    
    map1 = count_char(s1)
    map2 = count_char(s2)
    
    if len(s1) == len(s2):
        counter = 0
        for key in map2.keys():
            if key not in map1:
                counter += map2[key]
            else:
                counter += max(0, map2[key]-map1[key])
        print(counter)
    else:
        print(-1)
