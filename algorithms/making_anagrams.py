# HackerRank 'Making Anagrams' problem

a = input().strip()
b = input().strip()

for c in a:
    if c in b:
        a_pos = a.find(c)
        a = a[:a_pos] + a[a_pos+1:]

        b_pos = b.find(c)
        b = b[:b_pos] + b[b_pos+1:]

        
print(len(a+b))
