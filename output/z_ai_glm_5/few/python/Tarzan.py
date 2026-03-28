import sys

sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        d = int(next(iterator))
    except StopIteration:
        return

    trees = []
    for _ in range(n):
        x = int(next(iterator))
        y = int(next(iterator))
        trees.append((x, y))

    d_sq = d * d
    
    # Grafo implícito com DFS iterativo para evitar estouro de pilha (embora o limite tenha sido aumentado)
    # e para garantir performance.
    visited = [False] * n
    stack = [0]
    visited[0] = True
    count = 1
    
    while stack:
        u = stack.pop()
        x1, y1 = trees[u]
        
        for v in range(n):
            if not visited[v]:
                x2, y2 = trees[v]
                dx = x1 - x2
                dy = y1 - y2
                dist_sq = dx * dx + dy * dy
                
                if dist_sq <= d_sq:
                    visited[v] = True
                    stack.append(v)
                    count += 1
    
    if count == n:
        sys.stdout.write('S\n')
    else:
        sys.stdout.write('N\n')

if __name__ == '__main__':
    solve()