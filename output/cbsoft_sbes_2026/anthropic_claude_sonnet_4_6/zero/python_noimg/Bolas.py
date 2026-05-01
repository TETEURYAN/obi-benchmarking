from itertools import permutations

balls = list(map(int, input().split()))

def valid(seq):
    for i in range(len(seq)-1):
        if seq[i] == seq[i+1]:
            return False
    return True

found = False
for perm in permutations(balls):
    if valid(perm):
        found = True
        break

print("S" if found else "N")