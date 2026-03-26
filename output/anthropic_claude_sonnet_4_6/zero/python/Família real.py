
import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    N = int(input_data[idx]); idx += 1
    M = int(input_data[idx]); idx += 1
    
    parent = [0] * (N + 1)
    for i in range(1, N + 1):
        parent[i] = int(input_data[idx]); idx += 1
    
    attended = set()
    for i in range(M):
        attended.add(int(input_data[idx])); idx += 1
    
    # BFS to find generation of each descendant
    # King is 0, generation 1 = children of king
    generation = [0] * (N + 1)
    
    # Build children list
    children = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        children[parent[i]].append(i)
    
    # BFS from king (0)
    queue = deque()
    queue.append(0)
    gen_level = {0: 0}
    
    while queue:
        node = queue.popleft()
        for child in children[node]:
            gen_level[child] = gen_level[node] + 1
            generation[child] = gen_level[node] + 1
            queue.append(child)
    
    # Find max generation
    max_gen = max(generation[1:N+1]) if N > 0 else 0
    
    # Count total and attended per generation
    total = [0] * (max_gen + 1)
    att = [0] * (max_gen + 1)
    
    for i in range(1, N + 1):
        g = generation[i]
        total[g] += 1
        if i in attended:
            att[g] += 1
    
    results = []
    for g in range(1, max_gen + 1):
        if total[g] > 0:
            pct = att[g] / total[g] * 100.0
            results.append(f"{pct:.2f}")
    
    print(' '.join(results))

solve()
