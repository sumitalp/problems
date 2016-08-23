# Hacker Rank Pairs problem

def pairs(a,k):
    # a is the list of numbers and k is the difference value
    answer = 0
    s = set(a)

    for v in s:
        if v+k in s:
            answer += 1
        
    return answer
