# Hackerrank Bigger is Greater problem

def next_permutation(arr):
    # Find non-increasing suffix
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    if i <= 0:
        return None
    
    # Find successor to pivot
    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]

    # Reverse suffix
    arr[i : ] = arr[len(arr) - 1 : i - 1 : -1]
    return ''.join(arr)

t = int(input().strip())

for i in range(t):
    n = input().strip().lower()
    p = next_permutation(list(n))
    if p is not None:
        print(p)
    else:
        print('no answer')
