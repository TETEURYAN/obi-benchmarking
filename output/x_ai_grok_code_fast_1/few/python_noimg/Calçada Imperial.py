import sys

data = sys.stdin.read().split()
N = int(data[0])
V = [int(x) for x in data[1:]]

from collections import defaultdict
groups = defaultdict(int)
for i in range(N):
    if i == 0 or V[i] != V[i-1]:
        groups[V[i]] += 1
max_single = max(groups.values()) if groups else 0

ans = max_single
for a in range(1, N+1):
    for b in range(a+1, N+1):
        dp0 = 0
        dp1 = 0
        for v in V:
            if v == a:
                dp0 = max(dp0, dp1 + 1)
            if v == b:
                dp1 = max(dp1, dp0 + 1)
        ans = max(ans, dp0, dp1)

print(ans)