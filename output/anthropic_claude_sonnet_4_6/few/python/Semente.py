import sys

data = sys.stdin.read().split()
F = int(data[0])
R = int(data[1])
drops = [int(data[i+2]) for i in range(R)]

# The answer is the maximum of:
# 1. Distance from leftmost drop to left edge: drops[0] - 1
# 2. Distance from rightmost drop to right edge: F - drops[-1]
# 3. For each gap between consecutive drops: ceil((drops[i+1] - drops[i]) / 2)

ans = drops[0] - 1
ans = max(ans, F - drops[-1])

for i in range(R - 1):
    gap = drops[i+1] - drops[i]
    ans = max(ans, (gap) // 2)

print(ans)