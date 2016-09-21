# HackerRank 'Two String' problem

t = int(input())

for _ in range(t):
    a = input()
    b = input()
    
    if len(set(a)&set(b)) > 0:
        print('YES')
    else:
        print('NO')
