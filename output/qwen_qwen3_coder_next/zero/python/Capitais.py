
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    
    # Construir o grafo
    graph = [[] for _ in range(n + 1)]
    degree = [0] * (n + 1)
    
    idx = 1
    for _ in range(n - 1):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        graph[u].append(v)
        graph[v].append(u)
        degree[u] += 1
        degree[v] += 1
    
    # Identificar as capitais: são as cidades com grau 1 (capitais)
    capitals = []
    for i in range(1, n + 1):
        if degree[i] == 1:
            capitals.append(i)
    
    # Se houver apenas 2 cidades, resposta é 1
    if n == 2:
        print(1)
        return
    
    # Para cada capital, fazer BFS para encontrar a menor distância até outra capital
    min_dist = float('inf')
    
    for start in capitals:
        visited = [False] * (n + 1)
        queue = deque()
        queue.append((start, 0))
        visited[start] = True
        
        while queue:
            node, dist = queue.popleft()
        
            # Se encontrou outra capital (grau 1 e não é a própria)
            if node != start and degree[node] == 1:
                if dist < min_dist:
                    min_dist = dist
                break  # Como BFS encontra a menor distância, podemos parar ao achar a primeira outra capital
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, dist + 1))
    
    print(min_dist)

if __name__ == "__main__":
    main()
