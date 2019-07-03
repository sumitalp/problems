# HackerRank 'Palindrome Index' problem

def is_palindrome(x):
    if x == x[::-1]:
        return True
    return False

def palindrome_index(s):
    for idx in range((len(s)+1)//2):
        if s[idx] != s[len(s)-idx-1]:
            if is_palindrome(s[:idx]+s[idx+1:]):
                return idx
            else:
                return len(s)-idx-1
    return -1

T = int(input())

for i in range(T):
    S = input().strip()
    
    print(palindrome_index(S))
