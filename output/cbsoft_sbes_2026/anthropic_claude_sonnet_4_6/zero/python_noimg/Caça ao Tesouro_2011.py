n, k = map(int, input().split())

clues = []
for _ in range(k):
    x, y, d = map(int, input().split())
    clues.append((x, y, d))

possible = []
for tx in range(n):
    for ty in range(n):
        valid = True
        for (cx, cy, d) in clues:
            if abs(tx - cx) + abs(ty - cy) != d:
                valid = False
                break
        if valid:
            possible.append((tx, ty))

if len(possible) == 1:
    print(possible[0][0], possible[0][1])
else:
    print(-1, -1)