# Hackerrank Funny String problem
t = int(input())

for _ in range(t):
    s = input()
    rs = s[::-1]
    
    for i in range(1,len(s)):
        diff_one = ord(s[i]) - ord(s[i-1])
        diff_two = ord(rs[i]) - ord(rs[i-1])
        
        if abs(diff_one) != abs(diff_two):
            print('Not Funny')
            break
    else:
        print('Funny')
