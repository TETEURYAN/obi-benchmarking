
import sys
from collections import defaultdict

input = sys.stdin.read
data = input().split()

N = int(data[0])
A = list(map(int, data[1:]))

positions = defaultdict(list)
for i in range(N):
    positions[A[i]].append(i)

max_h = max(A)
dp = [0] * (max_h + 1)
last = [-1] * (max_h + 1)

for h in range(1, max_h + 1):
    if not positions[h]:
        dp[h] = dp[h-1]
        last[h] = last[h-1]
        continue
    
    pos = positions[h]
    m = len(pos)
    best = dp[h-1]
    best_last = last[h-1]
    
    if m >= 2:
        prev_dp = dp[h-1]
        prev_last = last[h-1]
        
        for i in range(m):
            curr = pos[i]
            if prev_last < curr:
                best = max(best, prev_dp + 1)
                best_last = max(best_last, curr)
    
    if m >= 1:
        curr = pos[0]
        if last[h-1] < curr:
            if dp[h-1] + 1 > best:
                best = dp[h-1] + 1
                best_last = curr
            elif dp[h-1] + 1 == best:
                best_last = max(best_last, curr)
    
    dp[h] = best
    last[h] = best_last

print(dp[max_h])
