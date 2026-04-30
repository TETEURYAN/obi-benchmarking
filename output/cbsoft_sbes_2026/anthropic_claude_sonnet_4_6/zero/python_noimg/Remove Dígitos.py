from collections import deque

def solve():
    N = int(input())
    
    dist = [-1] * (N + 1)
    dist[N] = 0
    queue = deque([N])
    
    while queue:
        curr = queue.popleft()
        if curr == 0:
            print(dist[0])
            return
        
        digits = set(int(d) for d in str(curr) if d != '0')
        
        for d in digits:
            nxt = curr - d
            if nxt >= 0 and dist[nxt] == -1:
                dist[nxt] = dist[curr] + 1
                queue.append(nxt)
    
    print(dist[0])

solve()