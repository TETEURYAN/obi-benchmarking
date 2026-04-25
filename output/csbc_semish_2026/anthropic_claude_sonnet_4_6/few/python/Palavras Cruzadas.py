import sys

data = sys.stdin.read().split()
horiz = data[0]
vert = data[1]

best_h = -1
best_v = -1

for i, ch in enumerate(horiz):
    for j, cv in enumerate(vert):
        if ch == cv:
            # We want rightmost in horiz (largest i), then lowest in vert (largest j)
            if i > best_h or (i == best_h and j > best_v):
                best_h = i
                best_v = j

if best_h == -1:
    print(-1, -1)
else:
    print(best_h + 1, best_v + 1)