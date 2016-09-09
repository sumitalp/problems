# Hacker Rank 'Fibonacci Modified' problem

t1, t2, n = input().strip().split()
t1, t2, n = [int(t1), int(t2), int(n)]

def modified_fibonacci(n):
    global t1, t2
    if 0<=n<=1:
        return t1
    elif n==2:
        return t2
    else:
        return modified_fibonacci(n-2) + modified_fibonacci(n-1)**2
    
print(modified_fibonacci(n))
