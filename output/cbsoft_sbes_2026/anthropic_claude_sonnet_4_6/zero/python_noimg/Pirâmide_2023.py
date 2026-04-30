from itertools import permutations

weights = list(map(int, input().split()))

found = False
for perm in permutations(weights):
    floor1 = perm[0] + perm[1] + perm[2]
    floor2 = perm[3] + perm[4]
    floor3 = perm[5]
    if floor1 == floor2 == floor3:
        found = True
        break

print('S' if found else 'N')