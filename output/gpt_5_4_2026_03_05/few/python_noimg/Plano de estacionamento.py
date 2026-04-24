import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n = data[0]
m = data[1]
v_list = data[2:2 + m]

parent = list(range(n + 1))

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

ans = 0
for v in v_list:
    spot = find(v)
    if spot == 0:
        break
    ans += 1
    parent[spot] = find(spot - 1)

print(ans)