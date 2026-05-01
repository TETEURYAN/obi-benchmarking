import sys

sys.setrecursionlimit(1_000_000)

input = sys.stdin.readline

N = int(input())

children = [[]]          # adjacency list
parent = [-1]
depth = [0]              # depth in edges from root
name_len = [0]           # length of folder name
files_direct = [0]       # number of files directly in this folder
sum_file_len_direct = [0]# sum of lengths of direct file names

folder_id = {}           # full path of folder -> id

total_root = 0

for _ in range(N):
    path = input().strip()
    parts = path.split('/')
    total_root += len(path)

    cur_path = ""
    cur = 0
    for comp in parts[:-1]:
        if cur_path:
            cur_path += '/' + comp
        else:
            cur_path = comp
        nxt = folder_id.get(cur_path)
        if nxt is None:
            nxt = len(children)
            folder_id[cur_path] = nxt
            children.append([])
            parent.append(cur)
            depth.append(depth[cur] + 1)
            name_len.append(len(comp))
            files_direct.append(0)
            sum_file_len_direct.append(0)
            children[cur].append(nxt)
        cur = nxt

    files_direct[cur] += 1
    sum_file_len_direct[cur] += len(parts[-1])

m = len(children)

sub_files = [0] * m
sub_sum_names = [0] * m
sum_depth_files = [0] * m

order = [0]
for u in order:
    for v in children[u]:
        order.append(v)

for u in reversed(order):
    sf = files_direct[u]
    ss = sum_file_len_direct[u]
    sd = files_direct[u] * depth[u]
    for v in children[u]:
        sf += sub_files[v]
        ss += sub_sum_names[v]
        sd += sum_depth_files[v]
    sub_files[u] = sf
    sub_sum_names[u] = ss
    sum_depth_files[u] = sd

ans = total_root

for r in range(1, m):
    inside = sub_files[r]
    outside = N - inside

    # Sum of lengths of all folder names on paths from r to files in its subtree
    inside_folder_chars = sum_depth_files[r] - inside * depth[r]

    # Cost for files inside subtree of r:
    # file names + slashes between remaining folders/file + folder name chars
    cost_inside = sub_sum_names[r] + inside_folder_chars + (sum_depth_files[r] - inside * depth[r])

    # Cost for files outside subtree of r:
    # original root-based cost + replace removed prefix by ../ repeated depth[r] times
    cost_outside = (total_root - (sub_sum_names[r] + sum_depth_files[r] + sub_files[r])) + 3 * depth[r] * outside

    total = cost_inside + cost_outside
    if total < ans:
        ans = total

print(ans)