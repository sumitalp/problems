# HackerRank 'Love Letter Mystery' problem

for _ in range(t):
        s = list(input())
        reductions = 0
        for i in range(0,len(s)//2):
            reductions += abs(ord(s[i]) - ord(s[-1-i]))
        print (reductions)
