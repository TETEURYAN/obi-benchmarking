
import sys
from collections import defaultdict

def dfs(node, graph, used, edges):
    for i in range(len(graph[node])):
        if not used[node][i]:
            used[node][i] = True
            neighbor = graph[node][i]
            for j in range(len(graph[neighbor])):
                if graph[neighbor][j] == node and not used[neighbor][j]:
                    used[neighbor][j] = True
                    break
            dfs(neighbor, graph, used, edges)
            edges[0] += 1

def can_form_domino(tiles):
    if not tiles:
        return True
    graph = defaultdict(list)
    for a, b in tiles:
        graph[a].append(b)
        graph[b].append(a)
    
    degrees = {i: len(graph[i]) for i in range(7)}
    odd_count = sum(1 for d in degrees.values() if d % 2 == 1)
    if odd_count not in (0, 2):
        return False
    
    start = next((i for i in range(7) if degrees[i] > 0), None)
    if start is None:
        return True
    
    used = {i: [False] * len(graph[i]) for i in graph}
    edges_used = [0]
    dfs(start, graph, used, edges_used)
    
    total_edges = len(tiles)
    return edges_used[0] == total_edges

def main():
    input = sys.stdin.read
    data = input().split()
    index = 0
    test_num = 1
    while True:
        N = int(data[index])
        index += 1
        if N == 0:
            break
        tiles = []
        for _ in range(N):
            x = int(data[index])
            y = int(data[index + 1])
            index += 2
            tiles.append((min(x, y), max(x, y)))
        
        possible = can_form_domino(tiles)
        
        print(f"Teste {test_num}")
        print("sim" if possible else "nao")
        print()
        test_num += 1

if __name__ == "__main__":
    main()
