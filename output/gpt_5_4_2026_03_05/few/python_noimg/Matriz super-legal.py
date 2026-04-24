import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

L = data[0]
C = data[1]
vals = data[2:]

A = [vals[i*C:(i+1)*C] for i in range(L)]

if L < 2 or C < 2:
    print(0)
    sys.exit()

B = [[0] * (C - 1) for _ in range(L - 1)]
for i in range(L - 1):
    row0 = A[i]
    row1 = A[i + 1]
    brow = B[i]
    for j in range(C - 1):
        brow[j] = row0[j] + row1[j + 1] - row0[j + 1] - row1[j]

heights = [0] * (C - 1)
best = 0

for i in range(L - 1):
    brow = B[i]
    for j in range(C - 1):
        if brow[j] <= 0:
            heights[j] += 1
        else:
            heights[j] = 0

    stack = []
    for j in range(C):
        cur = heights[j] if j < C - 1 else 0
        start = j
        while stack and stack[-1][1] >= cur:
            pos, h = stack.pop()
            if h > 0:
                width = j - pos
                area = (h + 1) * (width + 1)
                if area > best:
                    best = area
            start = pos
        stack.append((start, cur))

print(best)