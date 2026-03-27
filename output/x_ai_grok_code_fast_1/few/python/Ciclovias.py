import sys
sys.setrecursionlimit(200000)
input_data = sys.stdin.read().split()
N = int(input_data[0])
M = int(input_data[1])
adj = [[] for _ in range(N+1)]
idx = 2
for _ in range(M):
    a = int(input_data[idx])
    b = int(input_data[idx+1])
    adj[a].append(b)
    adj[b].append(a)
    idx += 2
from functools import lru_cache
@lru_cache(maxsize=None)
def dfs(v, parent, last_odd, last_even, is_odd):
    max_len = 1
    for u in adj[v]:
        if u == parent:
            continue
        if is_odd:
            if u > last_even:
                new_last_even = u
                new_last_odd = last_odd
                max_len = max(max_len, 1 + dfs(u, v, new_last_odd, new_last_even, False))
        else:
            if u > last_odd:
                new_last_odd = u
                new_last_even = last_even
                max_len = max(max_len, 1 + dfs(u, v, new_last_odd, new_last_even, True))
    return max_len
result = []
for i in range(1, N+1):
    r = dfs(i, -1, i, -1, True)
    result.append(str(r))
print(' '.join(result))