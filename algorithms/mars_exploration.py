# Hackerrank Mars Exploration problem
S = input().strip()
counter = 0
expected_s = 'SOS' * int(len(S)/3)

for i in range(len(S)):
    if S[i] != expected_s[i]:
        counter += 1

print(counter)
