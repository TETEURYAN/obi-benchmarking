import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    K1 = int(next(it))
    K2 = int(next(it))
    P = int(next(it))
    
    adj_metro = [[] for _ in range(N)]
    for _ in range(K1):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj_metro[u].append(v)
        adj_metro[v].append(u)
    
    adj_bus = [[] for _ in range(N)]
    for _ in range(K2):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj_bus[u].append(v)
        adj_bus[v].append(u)
    
    A = int(next(it)) - 1
    B = int(next(it)) - 1
    
    total_states = 3 * N
    dist = [-1] * total_states
    
    start_idx = A
    dist[start_idx] = 0
    dq = deque()
    dq.append((A, 0))
    
    while dq:
        u, s = dq.popleft()
        d = dist[u + s * N]
        # Metrô (sistema 1)
        if adj_metro[u]:
            t = 1
            custo = 0 if s == t else 1
            for v in adj_metro[u]:
                nidx = v + t * N
                if dist[nidx] == -1:
                    dist[nidx] = d + custo
                    if custo == 0:
                        dq.appendleft((v, t))
                    else:
                        dq.append((v, t))
        # Ônibus (sistema 2)
        if adj_bus[u]:
            t = 2
            custo = 0 if s == t else 1
            for v in adj_bus[u]:
                nidx = v + t * N
                if dist[nidx] == -1:
                    dist[nidx] = d + custo
                    if custo == 0:
                        dq.appendleft((v, t))
                    else:
                        dq.append((v, t))
    
    ans = -1
    for s in (1, 2):
        idx = B + s * N
        if dist[idx] != -1:
            if ans == -1 or dist[idx] < ans:
                ans = dist[idx]
    
    if ans == -1:
        print(-1)
    else:
        print(ans * P)

if __name__ == "__main__":
    main()