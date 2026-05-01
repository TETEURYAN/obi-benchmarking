import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        N = int(next(iterator))
        E = int(next(iterator))
        S = int(next(iterator))
        M = int(next(iterator))
    except StopIteration:
        return

    adj = [[] for _ in range(N)]
    for _ in range(M):
        try:
            A = int(next(iterator))
            B = int(next(iterator))
            T = int(next(iterator))
            adj[A].append((B, T))
        except StopIteration:
            break

    if E == S:
        print(0)
        return

    # dist[node][time % 3] stores the minimum time to reach node at that time mod.
    # -1 indicates unvisited.
    dist = [[-1] * 3 for _ in range(N)]
    
    queue = deque()
    queue.append((E, 0))
    dist[E][0] = 0

    while queue:
        u, m = queue.popleft()
        current_time = dist[u][m]

        for v, typ in adj[u]:
            # Check if the street is open at current_time.
            # typ 1: opens on multiples of 3 (m == 0).
            # typ 0: closes on multiples of 3 (m != 0).
            
            is_open = False
            if typ == 1:
                if m == 0:
                    is_open = True
            else: # typ == 0
                if m != 0:
                    is_open = True
            
            if is_open:
                next_time = current_time + 1
                next_m = next_time % 3
                
                if dist[v][next_m] == -1:
                    dist[v][next_m] = next_time
                    if v == S:
                        print(next_time)
                        return
                    queue.append((v, next_m))

    print('*')

if __name__ == '__main__':
    solve()