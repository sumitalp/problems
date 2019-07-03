# Codility Lesson: CyclicRotation problem

def solution(A, K):
    # write your code in Python 2.7
    for i in xrange(K):
        A = A[-1:] + A[:len(A)-1]
        
    return A
