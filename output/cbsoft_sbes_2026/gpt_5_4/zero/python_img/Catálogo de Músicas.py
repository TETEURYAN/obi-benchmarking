import sys

sys.setrecursionlimit(1_000_000)

input = sys.stdin.readline

N = int(input())

name_len = [0]          # comprimento do nome da pasta
parent = [-1]           # pai da pasta
depth = [0]             # profundidade em número de pastas desde a raiz
sum_folder = [0]        # soma dos comprimentos dos nomes das pastas no caminho raiz->nó
children = [[]]         # filhos pastas
folder_maps = [dict()]  # mapa nome->id para cada pasta

files_direct = [0]      # quantidade de arquivos diretamente na pasta
files_name_sum = [0]    # soma dos comprimentos dos nomes dos arquivos diretamente na pasta

for _ in range(N):
    parts = input().strip().split('/')
    cur = 0
    for part in parts[:-1]:
        mp = folder_maps[cur]
        nxt = mp.get(part)
        if nxt is None:
            nxt = len(parent)
            mp[part] = nxt
            parent.append(cur)
            l = len(part)
            name_len.append(l)
            depth.append(depth[cur] + 1)
            sum_folder.append(sum_folder[cur] + l)
            children.append([])
            folder_maps.append({})
            files_direct.append(0)
            files_name_sum.append(0)
            children[cur].append(nxt)
        cur = nxt
    fname = parts[-1]
    files_direct[cur] += 1
    files_name_sum[cur] += len(fname)

M = len(parent)

sub_files = [0] * M
sub_file_name_sum = [0] * M
sum_depth_files = [0] * M
sum_folder_files = [0] * M

order = [0]
for v in order:
    order.extend(children[v])

for v in reversed(order):
    total_f = files_direct[v]
    total_name = files_name_sum[v]
    total_depth = files_direct[v] * depth[v]
    total_folder_sum = files_direct[v] * sum_folder[v]
    for c in children[v]:
        total_f += sub_files[c]
        total_name += sub_file_name_sum[c]
        total_depth += sum_depth_files[c]
        total_folder_sum += sum_folder_files[c]
    sub_files[v] = total_f
    sub_file_name_sum[v] = total_name
    sum_depth_files[v] = total_depth
    sum_folder_files[v] = total_folder_sum

best = 10**30

for r in range(M):
    inside = sub_files[r]
    outside = N - inside

    total = 0
    total += sub_file_name_sum[0]
    total += sum_folder_files[0] - inside * sum_folder[r]
    total += sum_depth_files[0] - inside * depth[r]
    total += outside * (3 * depth[r])

    if total < best:
        best = total

print(best)