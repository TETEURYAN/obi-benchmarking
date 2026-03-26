import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx]); idx += 1
    M = int(data[idx]); idx += 1
    
    parent = [0] * (N + 1)
    for i in range(1, N + 1):
        parent[i] = int(data[idx]); idx += 1
    
    attended = set()
    for _ in range(M):
        attended.add(int(data[idx])); idx += 1
    
    # BFS from king (0) to find generation of each descendant
    generation = [0] * (N + 1)
    children = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        children[parent[i]].append(i)
    
    # BFS
    queue = deque()
    queue.append(0)
    gen_total = {}
    gen_attended = {}
    
    while queue:
        node = queue.popleft()
        for child in children[node]:
            g = generation[node] + 1
            generation[child] = g
            if g not in gen_total:
                gen_total[g] = 0
                gen_attended[g] = 0
            gen_total[g] += 1
            if child in attended:
                gen_attended[g] += 1
            queue.append(child)
    
    if not gen_total:
        print()
        return
    
    max_gen = max(gen_total.keys())
    result = []
    for g in range(1, max_gen + 1):
        total = gen_total.get(g, 0)
        att = gen_attended.get(g, 0)
        if total == 0:
            pct = 0.0
        else:
            pct = att / total * 100.0
        result.append(f"{pct:.2f}")
    
    print(' '.join(result))

main()