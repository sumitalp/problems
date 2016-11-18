# HackerRank problem 'Jumping on clouds revisited'

def solveCloudRevisited(c, n, k):
    pos = 0
    cnt = 0
 
    while cnt == 0 or pos != 0:
        pos += k
        pos %= n
        if c[pos] == 0:
            cnt += 1
        else:
            cnt += 3
     
    return 100 - cnt

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]

print(solveCloudRevisited(c,n,k))
