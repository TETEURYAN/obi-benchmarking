import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    F = [0] * (n + 1)
    for i in range(1, n + 1):
        F[i] = int(next(it))
    
    state = [0] * (n + 1)  # 0: unvisited, 1: visiting, 2: visited
    in_cycle = [False] * (n + 1)
    cycle_nodes = []
    cycle_pos = [0] * (n + 1)  # position in cycle for cycle nodes
    
    for i in range(1, n + 1):
        if state[i] != 0:
            continue
        path = []
        u = i
        while state[u] == 0:
            state[u] = 1
            path.append(u)
            u = F[u]
        if state[u] == 1:  # cycle found
            idx = path.index(u)
            cycle = path[idx:]
            for v in cycle:
                in_cycle[v] = True
                cycle_pos[v] = len(cycle_nodes)
                cycle_nodes.append(v)
        for v in path:
            state[v] = 2
    
    k = len(cycle_nodes)
    
    # Build reverse graph
    inverse = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        inverse[F[i]].append(i)
    
    d = [-1] * (n + 1)  # distance to cycle
    c = [0] * (n + 1)   # cycle entry node
    q = deque()
    for v in cycle_nodes:
        d[v] = 0
        c[v] = v
        q.append(v)
    
    while q:
        u = q.popleft()
        for v in inverse[u]:
            if d[v] == -1:
                d[v] = d[u] + 1
                c[v] = c[u]
                q.append(v)
    
    q_num = int(next(it))
    out_lines = []
    for _ in range(q_num):
        a = int(next(it))
        b = int(next(it))
        if a == b:
            out_lines.append("0")
        elif c[a] == c[b]:
            out_lines.append(str(abs(d[a] - d[b])))
        else:
            pos_a = cycle_pos[c[a]]
            pos_b = cycle_pos[c[b]]
            d_ab = (pos_b - pos_a) % k
            d_ba = k - d_ab
            t1 = max(d[b], d_ab + d[a])
            t2 = max(d[a], d_ba + d[b])
            out_lines.append(str(min(t1, t2)))
    
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()