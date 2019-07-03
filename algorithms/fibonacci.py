def fib1(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))


def fib2(n):
    a,b = 0,1
    yield a
    yield b
    while True:
        a,b = b, a+b
        yield b

def fib3(n):
    return (4 << n*(3+n)) // ((4 << 2*n) - (2 << n) - 1) & ((2 << n) - 1)

# This is quite efficient, using O(log n) basic arithmetic operations.
def fib4(n):
    return pow(2 << n, n+1, (4 << 2*n) - (2 << n) - 1) % (2 << n)

if __name__=='__main__':
    x = 8
    y = fib2(x)
    for i in range(8,0,-1):
        print(next(y))
