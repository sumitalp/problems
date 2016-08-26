# Hacker Rank 'Compare the Triplets' problem solved
import sys


a0,a1,a2 = input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]

alice_points = 0
bob_points = 0

def compare(a,b):
    global alice_points, bob_points
    if a<b:
        bob_points += 1
    elif a==b:
        pass
    else:
        alice_points += 1
        
        
compare(a0, b0)
compare(a1, b1)
compare(a2, b2)

print("{} {}".format(alice_points, bob_points))
