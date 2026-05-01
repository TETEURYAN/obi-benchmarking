
import sys
sys.setrecursionlimit(100000)

N = int(input())
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

diameter = 0
farthest = 1

def dfs1(u, p, dist):
    global diameter, farthest
    if dist > diameter:
        diameter = dist
        farthest = u
    for v in adj[u]:
        if v != p:
            dfs1(v, u, dist + 1)

dfs1(1, -1, 0)
diameter = 0
dfs1(farthest, -1, 0)
D = diameter

if D == 0:
    print(3)
    print(0)
    sys.exit(0)

def get_path(start, target):
    parent = [-1] * (N+1)
    stack = [start]
    parent[start] = -2
    found = False
    while stack and not found:
        u = stack.pop()
        for v in adj[u]:
            if parent[v] == -1:
                parent[v] = u
                stack.append(v)
                if v == target:
                    found = True
                    break
    path = []
    cur = target
    while cur != -2:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return path

path = get_path(farthest, 1)
center1 = path[D//2]
if D % 2 == 0:
    center2 = path[D//2 - 1]
else:
    center2 = -1

max_len = D + 1
count = 0

subtree = [0] * (N+1)
depth = [0] * (N+1)
is_on_diam = [False] * (N+1)
for u in path:
    is_on_diam[u] = True

def dfs_sub(u, p):
    subtree[u] = 1
    maxd = 0
    for v in adj[u]:
        if v != p and not is_on_diam[v]:
            depth[v] = depth[u] + 1
            dfs_sub(v, u)
            subtree[u] += subtree[v]
            maxd = max(maxd, depth[v])
    if not is_on_diam[u]:
        depth[u] = maxd + 1 if maxd > 0 else 0

for u in path:
    depth[u] = 0
    for v in adj[u]:
        if not is_on_diam[v]:
            depth[v] = 1
            dfs_sub(v, u)

def get_max_down(u, p):
    mx = 0
    for v in adj[u]:
        if v != p and not is_on_diam[v]:
            mx = max(mx, depth[v])
    return mx

downs = [0] * (N+1)
downs[0] = get_max_down(path[0], path[1]) if D > 0 else 0
downs[D] = get_max_down(path[D], path[D-1]) if D > 0 else 0

for i in range(1, D):
    u = path[i]
    d1 = get_max_down(u, path[i-1])
    d2 = get_max_down(u, path[i+1])
    downs[i] = max(d1, d2)

max_arm = [0] * (D+1)
max_arm[0] = downs[0]
for i in range(1, D+1):
    max_arm[i] = max(max_arm[i-1], downs[i] + i)

max_arm_rev = [0] * (D+1)
max_arm_rev[D] = downs[D]
for i in range(D-1, -1, -1):
    max_arm_rev[i] = max(max_arm_rev[i+1], downs[i] + (D - i))

max_cycle = D + 1
ways = 0

def add_ways(val):
    global ways
    ways = (ways + val) % 1000000000

for i in range(D+1):
    u = path[i]
    non_diam = []
    for v in adj[u]:
        if not is_on_diam[v]:
            non_diam.append(depth[v])
    non_diam.sort(reverse=True)
    arm_left = max_arm[i-1] if i > 0 else 0
    arm_right = max_arm_rev[i+1] if i < D else 0
    base = 1 + max(arm_left, arm_right)
    if non_diam:
        c1 = non_diam[0]
        cyc1 = 1 + c1 + base
        if cyc1 > max_cycle:
            max_cycle = cyc1
            ways = 0
        if cyc1 == max_cycle:
            add_ways(subtree[u] - 1)
        if len(non_diam) >= 2:
            c2 = non_diam[1]
            cyc2 = 1 + c1 + c2 + 1
            if cyc2 > max_cycle:
                max_cycle = cyc2
                ways = 0
            if cyc2 == max_cycle:
                add_ways(1)
    else:
        cyc = base + 1
        if cyc > max_cycle:
            max_cycle = cyc
            ways = 0
        if cyc == max_cycle:
            add_ways(1)

if D % 2 == 1:
    mid = D // 2
    u = path[mid]
    v = path[mid+1]
    left_max = max_arm[mid]
    right_max = max_arm_rev[mid+1]
    base = 2 + max(left_max, right_max)
    non_u = []
    for x in adj[u]:
        if not is_on_diam[x]:
            non_u.append(depth[x])
    non_v = []
    for x in adj[v]:
        if not is_on_diam[x]:
            non_v.append(depth[x])
    non_u.sort(reverse=True)
    non_v.sort(reverse=True)
    if non_u and non_v:
        c1 = non_u[0] + non_v[0] + 2
        if c1 > max_cycle:
            max_cycle = c1
            ways = 0
        if c1 == max_cycle:
            add_ways(subtree[u] * subtree[v])
    if non_u and len(non_u) >= 2:
        c2 = non_u[0] + non_u[1] + 2
        if c2 > max_cycle:
            max_cycle = c2
            ways = 0
        if c2 == max_cycle:
            add_ways(1)
    if non_v and len(non_v) >= 2:
        c3 = non_v[0] + non_v[1] + 2
        if c3 > max_cycle:
            max_cycle = c3
            ways = 0
        if c3 == max_cycle:
            add_ways(1)

print(max_cycle)
print(ways)
