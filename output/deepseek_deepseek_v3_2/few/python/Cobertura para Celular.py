import sys
import math

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    
    n = int(data[0])
    towers = []
    idx = 1
    for i in range(n):
        x = int(data[idx])
        y = int(data[idx+1])
        towers.append((x, y))
        idx += 2
    A = int(data[idx])
    
    # Construir grafo: duas torres estão conectadas se a distância <= 2*A
    # (alcance de ambas torres se sobrepõe)
    adj = [[] for _ in range(n)]
    for i in range(n):
        xi, yi = towers[i]
        for j in range(i+1, n):
            xj, yj = towers[j]
            dist = math.hypot(xi - xj, yi - yj)
            if dist <= 2 * A:
                adj[i].append(j)
                adj[j].append(i)
    
    # DFS para verificar conectividade
    visited = [False] * n
    stack = [0]
    visited[0] = True
    connected_count = 1
    
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                connected_count += 1
                stack.append(v)
    
    print('S' if connected_count == n else 'N')

if __name__ == "__main__":
    main()