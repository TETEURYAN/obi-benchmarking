
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
pesos = list(map(int, data[1:]))
pesos.sort(reverse=True)

if N == 0:
    print("S")
    sys.exit(0)

max_peso = max(pesos)
if max_peso > 8:
    print("N")
    sys.exit(0)

def pode_transportar():
    from collections import deque
    state = tuple([0] * N)
    visited = set()
    queue = deque([state])
    visited.add(state)
    
    while queue:
        current = list(queue.popleft())
        if all(x == 1 for x in current):
            return True
        
        on_top = [i for i in range(N) if current[i] == 1]
        on_bottom = [i for i in range(N) if current[i] == 0]
        
        for i in on_bottom:
            for j in on_top:
                p = pesos[i]
                q = pesos[j]
                if abs(p - q) <= 8:
                    new_state = current[:]
                    new_state[i] = 1
                    new_state[j] = 0
                    new_tup = tuple(new_state)
                    if new_tup not in visited:
                        visited.add(new_tup)
                        queue.append(new_tup)
            
            p = pesos[i]
            if abs(p - 0) <= 8:
                new_state = current[:]
                new_state[i] = 1
                new_tup = tuple(new_state)
                if new_tup not in visited:
                    visited.add(new_tup)
                    queue.append(new_tup)
        
        for j in on_top:
            if abs(0 - pesos[j]) <= 8:
                new_state = current[:]
                new_state[j] = 0
                new_tup = tuple(new_state)
                if new_tup not in visited:
                    visited.add(new_tup)
                    queue.append(new_tup)
    
    return False

if pode_transportar():
    print("S")
else:
    print("N")
