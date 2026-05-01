
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
dp = [0] * (N + 1)
tree = [0] * (4 * (N + 1))

def update(idx, val, node=1, start=0, end=N):
    if start == end:
        tree[node] = val
        return
    mid = (start + end) // 2
    if idx <= mid:
        update(idx, val, node * 2, start, mid)
    else:
        update(idx, val, node * 2 + 1, mid + 1, end)
    tree[node] = max(tree[node * 2], tree[node * 2 + 1])

def query(left, right, node=1, start=0, end=N):
    if right < start or left > end:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return max(query(left, right, node * 2, start, mid),
               query(left, right, node * 2 + 1, mid + 1, end))

ans = 0
for h in range(1, max_h + 1):
    if h not in positions:
        continue
    pos = positions[h]
    updates = []
    for p in pos:
        prev = query(0, p)
        new_val = prev + 1
        updates.append((p, new_val))
        ans = max(ans, new_val)
    for p, val in updates:
        update(p, val)

print(ans)
