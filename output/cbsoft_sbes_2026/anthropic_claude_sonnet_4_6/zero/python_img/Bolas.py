from itertools import permutations

balls = list(map(int, input().split()))

found = False
for perm in set(permutations(balls)):
    valid = True
    for i in range(len(perm) - 1):
        if perm[i] == perm[i+1]:
            valid = False
            break
    if valid:
        found = True
        break

print("S" if found else "N")