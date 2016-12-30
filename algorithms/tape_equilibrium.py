# Codility Time Complexity Lesson: TapeEquilibrium problem
import sys


def solution1(A):
    # Time Complexity: O(N*N)
    min_diff = 0
    for i in range(1,len(A)):
        diff = abs(sum(A[:i]) - sum(A[i:]))

        if min_diff==0 or min_diff > diff:
            min_diff = diff

    return min_diff

def solution2(A):
    # Time Complexity: O(N)
    try: # Python 2
        min_diff = sys.maxint
    except:
        min_diff = sys.maxsize # Python 3
    total = sum(A)

    for i in range(len(A)-1):
        abs_diff = abs(total - 2*A[i])
        total -= 2*A[i]

        if min_diff>abs_diff:
            min_diff = abs_diff

    return min_diff 


if __name__=='__main__':
    A = [3,1,2,4,3]

    print(solution2(A))
