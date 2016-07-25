# Hackerrank Sherlock and the Beast problem
def sherlock(target):
    threes = 0
    fives = 0
    digits = target
    ret_str = ""
    
    while digits > 0:
        if digits % 3 == 0:
            fives = digits
            break
        digits -= 5
        
    threes = target - digits
    
    if digits < 0 or threes % 5 != 0:
        return -1
    
    if fives > 0:
        ret_str = ret_str + ("5" * fives)
    
    if threes > 0:
        ret_str = ret_str + ("3" * threes)
        
    return ret_str

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    print(sherlock(n))
