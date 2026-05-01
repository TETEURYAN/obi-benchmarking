import sys

data = list(map(int, sys.stdin.read().split()))
F, R = data[0], data[1]
pos = data[2:2 + R]

ans = max(pos[0] - 1, F - pos[-1])

for i in range(R - 1):
    gap = pos[i + 1] - pos[i]
    ans = max(ans, gap // 2)

print(ans)