# Hackerrank Gemstones problem

t = int(input())
all_elements = set(input())
     
for _ in range(t-1):
    all_elements &= set(input())

print(len(all_elements))
