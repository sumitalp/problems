# Codility 'Binary Gap' problem


# Solution: 1

def solution(N):
    # write your code in Python 2.7
    max_gap = 0
    curr_gap = 0
    
    while N > 0 and N%2 ==0:
        N //= 2
        
    while N > 0:
        r = N%2
        
        if r==0:
            # Inside gap
            curr_gap += 1
        else:
            # Gap ends
            if curr_gap != 0:
                max_gap = max(curr_gap, max_gap)
                curr_gap = 0
                
        N //= 2
    
    return max_gap



# Solution: 2

def solution(N):
    s = "{0:b}".format(N)
    max_gap = 0
    curr_gap = 0
    
    for i in s:
        if i=='0':
            curr_gap += 1
        if i=='1':
            if max_gap < curr_gap:
                max_gap = curr_gap
            curr_gap = 0
    return max_gap

# Worst Complexity O(log(n))
# Worst space complexity O(1)
