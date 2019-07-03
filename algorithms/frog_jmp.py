# Codility Time Complexity Lesson: FrogJmp problem
# Time and Space Complexity: O(1)

import math

def solution(X, Y, D):
    # write your code in Python 2.7
    return int(math.ceil( float(Y-X)/D ))


if __name__=='__main__':
    print(solution(10,85,30))
