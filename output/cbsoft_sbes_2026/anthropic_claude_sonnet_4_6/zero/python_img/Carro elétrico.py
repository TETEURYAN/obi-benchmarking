from collections import defaultdict

def solve():
    import sys
    from collections import deque
    
    input_data = sys.stdin.read().split()
    idx = 0
    
    X = int(input_data[idx]); idx += 1
    Y = int(input_data[idx]); idx += 1
    N = int(input_data[idx]); idx += 1
    A = int(input_data[idx]); idx += 1
    
    cities = []
    for i in range(N):
        x = int(input_data[idx]); idx += 1
        y = int(input_data[idx]); idx += 1
        cities.append((x, y))
    
    # Distance between two cities (Manhattan distance * 100)
    def dist(i, j):
        xi, yi = cities[i]
        xj, yj = cities[j]
        return (abs(xi - xj) + abs(yi - yj)) * 100
    
    # Build adjacency: cities reachable by car (dist <= A)
    # We need to find connected components where cities are connected if reachable by car
    # But "reachable by car" means there's a path through intermediate cities
    # Actually, the car can travel between cities along roads, stopping at intermediate cities to recharge
    # So two cities are reachable from each other by car if there's a path where each consecutive step <= A
    
    # Build graph where edge exists if dist(i,j) <= A
    # Then find connected components
    # The answer is: number of connected components - 1
    # Because from city 1, we need one flight to reach each new component
    
    # Wait, but we start at city 1, so we need (number of components - 1) flights
    # if city 1's component is one of them
    
    n = N
    
    # Build adjacency list for car travel
    adj = defaultdict(list)
    for i in range(n):
        for j in range(i+1, n):
            d = dist(i, j)
            if d <= A:
                adj[i].append(j)
                adj[j].append(i)
    
    # Find connected components using BFS
    visited = [False] * n
    components = 0
    
    for start in range(n):
        if not visited[start]:
            components += 1
            queue = deque([start])
            visited[start] = True
            while queue:
                node = queue.popleft()
                for neighbor in adj[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
    
    # Number of flights needed = components - 1
    # (we start at city 1 which is in one component, need to fly to each other component)
    print(components - 1)

solve()