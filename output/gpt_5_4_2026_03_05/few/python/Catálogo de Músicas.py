import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

n = int(data[0])

children = [[]]
parent = [-1]
name_len = [0]
depth = [0]
subtree_files = [0]
sum_file_depths = [0]
direct_file_cost = [0]

node_map = {}

def get_child(par, name):
    key = (par, name)
    v = node_map.get(key)
    if v is None:
        v = len(parent)
        node_map[key] = v
        parent.append(par)
        name_len.append(len(name))
        depth.append(depth[par] + 1)
        subtree_files.append(0)
        sum_file_depths.append(0)
        direct_file_cost.append(0)
        children.append([])
        children[par].append(v)
    return v

total_root_cost = 0

for i in range(1, n + 1):
    parts = data[i].split('/')
    cur = 0
    for s in parts[:-1]:
        cur = get_child(cur, s)
    flen = len(parts[-1])
    d = depth[cur] + 1
    subtree_files[cur] += 1
    sum_file_depths[cur] += d
    direct_file_cost[cur] += flen
    total_root_cost += sum(len(x) for x in parts) + (len(parts) - 1)

order = [0]
for u in order:
    for v in children[u]:
        order.append(v)

for u in reversed(order[1:]):
    p = parent[u]
    subtree_files[p] += subtree_files[u]
    sum_file_depths[p] += sum_file_depths[u]
    direct_file_cost[p] += direct_file_cost[u]

total_files = n
ans = total_root_cost

cost = [0] * len(parent)
cost[0] = total_root_cost

for u in order:
    cu = cost[u]
    if cu < ans:
        ans = cu
    for v in children[u]:
        inside = subtree_files[v] * (name_len[v] + 1)
        outside = (total_files - subtree_files[v]) * 3
        cost[v] = cu - inside + outside

print(ans)