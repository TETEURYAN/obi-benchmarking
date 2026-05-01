
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    f = [0] * (n + 1)
    for i in range(1, n + 1):
        f[i] = int(next(it))
    
    in_cycle = [False] * (n + 1)
    visited = [False] * (n + 1)
    cycle_nodes = []
    
    for i in range(1, n + 1):
        if not visited[i]:
            path = []
            current = i
            while True:
                if visited[current]:
                    if current in path:
                        idx = path.index(current)
                        cycle_nodes.extend(path[idx:])
                    break
                visited[current] = True
                path.append(current)
                current = f[current]
    
    for node in cycle_nodes:
        in_cycle[node] = True
    
    depth = [-1] * (n + 1)
    parent = [0] * (n + 1)
    for node in cycle_nodes:
        q = deque()
        q.append(node)
        depth[node] = 0
        parent[node] = 0
        while q:
            u = q.popleft()
            v = f[u]
            if not in_cycle[v] and depth[v] == -1:
                depth[v] = depth[u] + 1
                parent[v] = u
                q.append(v)
    
    q_count = int(next(it))
    out_lines = []
    for _ in range(q_count):
        a = int(next(it))
        b = int(next(it))
        if a == b:
            out_lines.append("0")
            continue
        
        if in_cycle[a] and in_cycle[b]:
            dist_a = 0
            dist_b = 0
            u = a
            while u != 0:
                if u == b:
                    break
                u = f[u]
                dist_a += 1
            if u == b:
                out_lines.append(str(dist_a))
                continue
            u = b
            while u != 0:
                if u == a:
                    break
                u = f[u]
                dist_b += 1
            if u == a:
                out_lines.append(str(dist_b))
                continue
            total = dist_a + dist_b
            out_lines.append(str(total))
            continue
        
        if in_cycle[a]:
            dist_b = 0
            u = b
            while u != 0 and not in_cycle[u]:
                u = f[u]
                dist_b += 1
            if u == 0:
                u = cycle_nodes[0]
            dist_a = 0
            temp = a
            while temp != u:
                temp = f[temp]
                dist_a += 1
            total = dist_a + dist_b
            out_lines.append(str(total))
            continue
        
        if in_cycle[b]:
            dist_a = 0
            u = a
            while u != 0 and not in_cycle[u]:
                u = f[u]
                dist_a += 1
            if u == 0:
                u = cycle_nodes[0]
            dist_b = 0
            temp = b
            while temp != u:
                temp = f[temp]
                dist_b += 1
            total = dist_a + dist_b
            out_lines.append(str(total))
            continue
        
        dist_a = 0
        u = a
        while u != 0 and not in_cycle[u]:
            u = f[u]
            dist_a += 1
        if u == 0:
            u = cycle_nodes[0]
        dist_b = 0
        v = b
        while v != 0 and not in_cycle[v]:
            v = f[v]
            dist_b += 1
        if v == 0:
            v = cycle_nodes[0]
        dist_uv = 0
        temp = u
        while temp != v:
            temp = f[temp]
            dist_uv += 1
        total = dist_a + dist_b + dist_uv
        out_lines.append(str(total))
    
    print('\n'.join(out_lines))

if __name__ == "__main__":
    main()
