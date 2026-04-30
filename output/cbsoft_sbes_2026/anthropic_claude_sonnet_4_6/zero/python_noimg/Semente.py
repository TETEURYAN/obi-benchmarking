F, R = map(int, input().split())
drops = list(map(int, input().split()))

# The answer is the maximum of:
# 1. Distance from leftmost drop to left edge (drop - 1)
# 2. Distance from rightmost drop to right edge (F - drop)
# 3. For each pair of adjacent drops, ceil((drop[i+1] - drop[i]) / 2)

ans = drops[0] - 1  # left edge
ans = max(ans, F - drops[-1])  # right edge

for i in range(len(drops) - 1):
    gap = drops[i+1] - drops[i]
    ans = max(ans, (gap) // 2)

print(ans)