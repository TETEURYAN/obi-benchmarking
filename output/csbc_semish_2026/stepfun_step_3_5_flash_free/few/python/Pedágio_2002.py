import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    test_num = 1
    out_lines = []
    while True:
        C = int(data[idx]); E = int(data[idx+1]); L = int(data[idx+2]); P = int(data[idx+3])
        idx += 4
        if C == 0 and E == 0 and L == 0 and P == 0:
            break
        adj = [[] for _ in range(C+1)]
        for _ in range(E):
            u = int(data[idx]); v = int(data[idx+1]); idx += 2
            adj[u].append(v)
            adj[v].append(u)
        dist = [-1] * (C+1)
        dist[L] = 0
        q = deque([L])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
        reachable = []
        for city in range(1, C+1):
            if city != L and dist[city] != -1 and dist[city] <= P:
                reachable.append(str(city))
        out_lines.append(f"Teste {test_num}")
        out_lines.append(" ".join(reachable))
        out_lines.append("")
        test_num += 1
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()