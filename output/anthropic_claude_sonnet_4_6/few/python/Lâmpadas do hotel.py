import sys
from collections import deque

data = sys.stdin.read().split()
IA, IB, FA, FB = int(data[0]), int(data[1]), int(data[2]), int(data[3])

# BFS to find minimum number of button presses
# State: (a, b)
# C1: toggles A
# C2: toggles both A and B

start = (IA, IB)
goal = (FA, FB)

if start == goal:
    print(0)
else:
    visited = {start: 0}
    queue = deque([(start, 0)])
    found = False
    while queue:
        (a, b), dist = queue.popleft()
        for na, nb in [(1-a, b), (1-a, 1-b)]:
            state = (na, nb)
            if state not in visited:
                visited[state] = dist + 1
                if state == goal:
                    print(dist + 1)
                    found = True
                    break
                queue.append((state, dist + 1))
        if found:
            break
    if not found:
        print(-1)