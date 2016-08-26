# Hacker Rank 'Caesar Chiper' problem solution

import sys


n = int(input().strip())
s = input().strip()
k = int(input().strip())

def encrypt_caesar(s, k):
    output = list(s)
    k %= (ord('z') - ord('a') + 1)

    for i, l in enumerate(output):
        if l.isalpha():
            if l.isupper():
                new_char = ord(l)+k
                if new_char > ord('Z'):
                    new_char = new_char - ord('Z') + ord('A') - 1
                output[i] = chr(new_char)
            else:
                new_char = ord(l)+k
                if new_char > ord('z'):
                    new_char = new_char - ord('z') + ord('a') - 1
                output[i] = chr(new_char)
    return ''.join(output)

print(encrypt_caesar(s, k))
