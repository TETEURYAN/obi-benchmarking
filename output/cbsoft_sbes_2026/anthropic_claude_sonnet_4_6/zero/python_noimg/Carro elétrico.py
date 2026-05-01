from collections import deque

def solve():
    import sys
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
    
    # Manhattan distance between cities (scaled by 100km per unit)
    # Distance between city i and city j = (|xi - xj| + |yi - yj|) * 100
    # Car can travel if distance <= A
    
    # Build graph: cities are connected by car if manhattan distance * 100 <= A
    # We need to find minimum number of flights to visit all cities starting from city 0 (1-indexed: city 1)
    
    # This is essentially: find connected components where cities are connected if reachable by car
    # Then find minimum number of flights = minimum spanning tree edges in component graph
    # But we need to visit ALL cities starting from city 1
    # 
    # Key insight: 
    # - Build a graph where cities are nodes
    # - Two cities are "car-connected" if you can travel between them using only car (possibly through intermediate cities)
    # - Connected components via car travel
    # - The number of flights needed = number of components that need to be reached by flight
    # - Since we start at city 1, we need to fly to each other component at least once
    # - But we can also use intermediate cities as hubs
    # 
    # Actually: BFS/DFS to find connected components where edge exists if distance <= A
    # Then minimum flights = (number of components - 1) since we start in component of city 1
    # But wait - we might need more flights if some components are only reachable through other components
    # No - we can always fly directly to any city, so minimum flights = number of components - 1
    
    # Wait, but the problem says "if distance to next city > autonomy, travel by plane"
    # The traveler can choose which city to fly to next
    # So minimum flights = number of connected components (by car) - 1
    # Because: visit all cities in component 1 by car, then fly to one city in each other component
    
    # Build adjacency for car travel
    # Two cities connected by car if manhattan distance (in road units) * 100 <= A
    # i.e., |xi - xj| + |yi - yj| <= A / 100
    
    threshold = A / 100.0  # in road units
    
    n = N
    adj = [[] for _ in range(n)]
    
    for i in range(n):
        for j in range(i+1, n):
            dist = abs(cities[i][0] - cities[j][0]) + abs(cities[i][1] - cities[j][1])
            if dist * 100 <= A:
                adj[i].append(j)
                adj[j].append(i)
    
    # Find connected components
    visited = [False] * n
    components = 0
    
    for start in range(n):
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
    
    # Minimum flights = components - 1
    print(components - 1)

solve()