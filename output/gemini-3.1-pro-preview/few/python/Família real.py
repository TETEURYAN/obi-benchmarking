import sys
from collections import deque

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
m = int(input_data[1])

adj = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    p = int(input_data[1 + i])
    adj[p].append(i)

attendees = []
for i in range(m):
    attendees.append(int(input_data[2 + n + i]))

depth = [-1] * (n + 1)
depth[0] = 0

q = deque([0])
max_depth = 0

while q:
    u = q.popleft()
    for v in adj[u]:
        depth[v] = depth[u] + 1
        if depth[v] > max_depth:
            max_depth = depth[v]
        q.append(v)

total_gen = [0] * (max_depth + 1)
attended_gen = [0] * (max_depth + 1)

for i in range(1, n + 1):
    if depth[i] != -1:
        total_gen[depth[i]] += 1

for att in attendees:
    if depth[att] != -1:
        attended_gen[depth[att]] += 1

ans = []
for g in range(1, max_depth + 1):
    if total_gen[g] > 0:
        pct = (attended_gen[g] * 100.0) / total_gen[g]
        ans.append(f"{pct:.2f}")
    else:
        ans.append("0.00")

print(" ".join(ans))