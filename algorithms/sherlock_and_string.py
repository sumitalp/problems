# HackerRank 'Sherlock and String' problem

from collections import Counter
 
 
def isValid(S):
    char_map = Counter(S)
    char_occurence_map = Counter(char_map.values())
 
    if len(char_occurence_map) == 1:
        return True

    if len(char_occurence_map) == 2:
        for v in char_occurence_map.values():
            if v == 1:
                return True
 
    return False
 
 
S = input()
if isValid(S):
    print("YES")
else:
    print("NO")

# Complexity: O(N)
# Space complexity: O(1)
