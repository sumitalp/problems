# Codility Lesson: PermMissingElem problem
# Time Complexity: O(N) or O(N * log(N))
# Space Complexity: O(1)


def solution(A):
    # write your code in Python 2.7
    N = len(A) + 1
    missing = ((N+1)*N)/2
    
    for i in A:
        missing -= i
        
    return missing

if __name__ == '__main__':
    A = [2,3,1,5]

    print(solution(A))

    A = []
    print(solution(A))
