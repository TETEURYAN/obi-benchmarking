import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
m = int(input_data[1])

adj = [[] for _ in range(n + 1)]
idx = 2
for _ in range(m):
    u = int(input_data[idx])
    v = int(input_data[idx+1])
    adj[u].append(v)
    adj[v].append(u)
    idx += 2

chosen = [False] * (n + 1)
ans = []

for i in range(n, 0, -1):
    can_choose = True
    for neighbor in adj[i]:
        if chosen[neighbor]:
            can_choose = False
            break
    if can_choose:
        chosen[i] = True
        ans.append(i)

ans.reverse()
print(len(ans))
print(*(ans))