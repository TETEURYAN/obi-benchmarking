h = input().strip()
v = input().strip()

best_h = -1
best_v = -1

for i, ch in enumerate(h):
    for j, cv in enumerate(v):
        if ch == cv:
            # We want maximum i (rightmost in h), then maximum j (lowest in v)
            if i > best_h or (i == best_h and j > best_v):
                best_h = i
                best_v = j

if best_h == -1:
    print(-1, -1)
else:
    print(best_h + 1, best_v + 1)