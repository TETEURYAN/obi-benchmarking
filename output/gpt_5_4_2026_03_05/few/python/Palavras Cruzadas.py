import sys

data = sys.stdin.read().split()
if len(data) < 2:
    sys.exit()

h = data[0]
v = data[1]

last_pos_h = {}
for i, ch in enumerate(h, 1):
    last_pos_h[ch] = i

best_h = -1
best_v = -1

for j, ch in enumerate(v, 1):
    if ch in last_pos_h:
        i = last_pos_h[ch]
        if i > best_h or (i == best_h and j > best_v):
            best_h = i
            best_v = j

print(best_h, best_v)