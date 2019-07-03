# HackerRank problem 'Jumping on the clouds'

def solveCloud(c, n):
    v = [100] * n
    v[0] = 0
 
    for i in range(1,n):
        
        if c[i] == 1:
            continue

        if i == 1:
            v[i] = v[i-1] + 1
        else:
            v[i] = min(v[i-1], v[i-2]) + 1
     
    return v[n-1]

n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]

print(solveCloud(c, n))
