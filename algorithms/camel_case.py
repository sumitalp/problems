#!/bin/python3
# Hacker Rank 'Camel Case' problem

import sys


s = input().strip()
total_words = 0

for i in range(len(s)):
    if s[i].islower() and i == 0:
        total_words += 1
    elif s[i].isupper():
        total_words += 1
        
print(total_words)
