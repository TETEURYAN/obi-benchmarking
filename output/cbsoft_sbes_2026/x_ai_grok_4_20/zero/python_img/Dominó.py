
import sys
from collections import defaultdict, deque

def can_form_domino_chain(dominoes):
    if not dominoes:
        return True
    
    graph = defaultdict(list)
    degrees = [0] * 7
    all_pieces = []
    
    for a, b in dominoes:
        graph[a].append(b)
        graph[b].append(a)
        degrees[a] += 1
        degrees[b] += 1
        all_pieces.append((min(a, b), max(a, b)))
    
    non_zero = [i for i in range(7) if degrees[i] > 0]
    if not non_zero:
        return True
    
    start = non_zero[0]
    for i in range(7):
        if degrees[i] % 2 == 1:
            start = i
            break
    
    visited = [False] * len(all_pieces)
    used_edges = defaultdict(int)
    
    def dfs(current):
        if sum(visited) == len(all_pieces):
            return True
        for i, (a, b) in enumerate(all_pieces):
            if visited[i]:
                continue
            if a == current or b == current:
                next_val = b if a == current else a
                edge_key = (min(a, b), max(a, b))
                if used_edges[edge_key] < all_pieces.count(edge_key):
                    used_edges[edge_key] += 1
                    visited[i] = True
                    if dfs(next_val):
                        return True
                    visited[i] = False
                    used_edges[edge_key] -= 1
        return False
    
    return dfs(start)

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
        
        dominoes = []
        for _ in range(N):
            x = int(data[index])
            y = int(data[index + 1])
            index += 2
            dominoes.append((x, y))
        
        possible = can_form_domino_chain(dominoes)
        
        print(f"Teste {test_num}")
        print("sim" if possible else "nao")
        print()
        test_num += 1

if __name__ == "__main__":
    main()
