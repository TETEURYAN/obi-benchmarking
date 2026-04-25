import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    idx = 0
    X = int(data[idx]); idx+=1
    Y = int(data[idx]); idx+=1
    N = int(data[idx]); idx+=1
    A = int(data[idx]); idx+=1
    
    cities = []
    for i in range(N):
        x = int(data[idx]); idx+=1
        y = int(data[idx]); idx+=1
        cities.append((x, y))
    
    # Distance between city i and city j (Manhattan distance * 100)
    def dist(i, j):
        xi, yi = cities[i]
        xj, yj = cities[j]
        return (abs(xi - xj) + abs(yi - yj)) * 100
    
    # Build graph: cities reachable by car (dist <= A)
    # We need to find connected components where cities are connected if dist <= A
    # But we can visit intermediate cities, so we need BFS/DFS on the graph
    # where edge exists if dist(i,j) <= A
    
    # Actually, we need to think about this more carefully.
    # The car can travel between cities if the road distance <= A.
    # The road distance is Manhattan distance * 100.
    # We can visit intermediate cities to recharge.
    # So two cities are reachable by car (without plane) if there's a path
    # through intermediate cities where each consecutive pair has dist <= A.
    
    # So we build a graph where edge(i,j) exists if dist(i,j) <= A,
    # then find connected components.
    # The number of plane trips = number of connected components - 1
    # (since we start at city 1 and need to visit all components)
    # Wait, but we need to visit ALL cities, so we need to connect all components.
    # Starting from city 1's component, each new component requires 1 plane trip.
    # But after flying to a new component, we can use car within that component.
    # So minimum plane trips = number of connected components - 1.
    
    # Build adjacency for BFS
    adj = [[] for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            d = dist(i, j)
            if d <= A:
                adj[i].append(j)
                adj[j].append(i)
    
    # Find connected components
    visited = [False] * N
    components = 0
    
    for start in range(N):
        if not visited[start]:
            components += 1
            queue = deque([start])
            visited[start] = True
            while queue:
                node = queue.popleft()
                for nb in adj[node]:
                    if not visited[nb]:
                        visited[nb] = True
                        queue.append(nb)
    
    # Minimum plane trips = components - 1
    print(components - 1)

solve()