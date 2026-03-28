import sys

input_data = sys.stdin.read().split()
idx = 0
E = int(input_data[idx])
idx += 1
I = int(input_data[idx])
idx += 1
V = int(input_data[idx])
idx += 1

adj = [[] for _ in range(E + 1)]
rev_adj = [[] for _ in range(E + 1)]
for _ in range(I):
    A = int(input_data[idx])
    B = int(input_data[idx + 1])
    adj[A].append(B)
    rev_adj[B].append(A)
    idx += 2

initial = set()
for _ in range(V):
    x = int(input_data[idx])
    initial.add(x)
    idx += 1

# compute ancestors
ancestors = [set() for _ in range(E + 1)]
sys.setrecursionlimit(200000)
def dfs(u, anc):
    anc.add(u)
    for v in rev_adj[u]:
        if v not in anc:
            dfs(v, anc)

for i in range(1, E + 1):
    anc = set()
    dfs(i, anc)
    ancestors[i] = anc

# compute depth
depth = [0] * (E + 1)
for i in range(1, E + 1):
    if rev_adj[i]:
        depth[i] = max(depth[j] for j in rev_adj[i]) + 1

# now, true set
true = set(initial)
changed = True
while changed:
    changed = False
    for B in list(true):
        if rev_adj[B]:
            causes = rev_adj[B]
            inter = ancestors[causes[0]].copy()
            for c in causes[1:]:
                inter &= ancestors[c]
            if inter:
                lca = max(inter, key=lambda x: depth[x])
                for a in ancestors[lca]:
                    if a not in true:
                        true.add(a)
                        changed = True
        # propagate forward
        for c in adj[B]:
            if c not in true:
                true.add(c)
                changed = True

# output
print(' '.join(map(str, sorted(true))))