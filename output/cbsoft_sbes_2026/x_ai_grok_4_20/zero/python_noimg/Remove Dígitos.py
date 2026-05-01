
from collections import deque

N = int(input().strip())

if N == 0:
    print(0)
else:
    queue = deque([N])
    dist = [float('inf')] * (N + 1)
    dist[N] = 0
    
    while queue:
        current = queue.popleft()
        if current == 0:
            print(dist[0])
            break
        
        # Obter dígitos únicos do número atual
        digits = set()
        temp = current
        while temp > 0:
            digits.add(temp % 10)
            temp //= 10
        
        for d in digits:
            if d == 0:
                continue
            next_val = current - d
            if next_val >= 0 and dist[next_val] == float('inf'):
                dist[next_val] = dist[current] + 1
                queue.append(next_val)
