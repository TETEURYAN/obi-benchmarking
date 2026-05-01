import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

N = int(input_data[0])
M = int(input_data[1])

P = [0] * (N * M)
idx = 2
for i in range(N * M):
    P[i] = int(input_data[idx])
    idx += 1

order = sorted(range(N * M), key=lambda x: P[x])

parent = list(range(N * M))
sum_power = P[:]
cells = [[i] for i in range(N * M)]
ans = [0] * (N * M)
processed = [False] * (N * M)

def find(i):
    root = i
    while parent[root] != root:
        root = parent[root]
    curr = i
    while curr != root:
        nxt = parent[curr]
        parent[curr] = root
        curr = nxt
    return root

for u in order:
    processed[u] = True
    r = u // M
    c = u % M
    
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M:
            v = nr * M + nc
            if processed[v]:
                v_comp = find(v)
                if u != v_comp:
                    if sum_power[v_comp] < P[u]:
                        for cell in cells[v_comp]:
                            ans[cell] = sum_power[v_comp]
                        cells[v_comp] = []
                    else:
                        if len(cells[u]) < len(cells[v_comp]):
                            cells[u], cells[v_comp] = cells[v_comp], cells[u]
                        cells[u].extend(cells[v_comp])
                        cells[v_comp] = []
                    
                    sum_power[u] += sum_power[v_comp]
                    parent[v_comp] = u

for i in range(N * M):
    if parent[i] == i and cells[i]:
        for cell in cells[i]:
            ans[cell] = sum_power[i]

out = []
for i in range(N):
    row_ans = ans[i * M : (i + 1) * M]
    out.append(" ".join(map(str, row_ans)))
print("\n".join(out))