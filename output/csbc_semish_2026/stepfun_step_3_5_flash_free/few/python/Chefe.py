import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    I = int(next(it))
    
    K = [0] * (N + 1)
    for i in range(1, N + 1):
        K[i] = int(next(it))
    
    parents = [[] for _ in range(N + 1)]
    children = [[] for _ in range(N + 1)]
    for _ in range(M):
        x = int(next(it))
        y = int(next(it))
        parents[y].append(x)
        children[x].append(y)
    
    # Topological sort (Kahn's algorithm)
    indegree = [0] * (N + 1)
    for v in range(1, N + 1):
        indegree[v] = len(parents[v])
    q = deque()
    for v in range(1, N + 1):
        if indegree[v] == 0:
            q.append(v)
    topo = []
    while q:
        u = q.popleft()
        topo.append(u)
        for v in children[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)
    
    # Compute ancestors_mask for each position
    ancestors_mask = [0] * (N + 1)
    for v in topo:
        mask = 0
        for pa in parents[v]:
            mask |= (1 << (pa - 1))
            mask |= ancestors_mask[pa]
        ancestors_mask[v] = mask
    
    # Initialize real and pos arrays
    real = list(range(N + 1))  # real[pos] = employee ID at that position
    pos = list(range(N + 1))    # pos[emp] = current position of employee
    
    output_lines = []
    for _ in range(I):
        typ = next(it)
        if typ == 'T':
            a = int(next(it))
            b = int(next(it))
            pa = pos[a]
            pb = pos[b]
            # Swap employees at positions pa and pb
            real[pa], real[pb] = real[pb], real[pa]
            # Swap positions of employees a and b
            pos[a], pos[b] = pos[b], pos[a]
        else:  # 'P'
            e = int(next(it))
            p = pos[e]
            mask = ancestors_mask[p]
            if mask == 0:
                output_lines.append('*')
            else:
                min_idade = None
                for q_pos in range(1, N + 1):
                    if mask & (1 << (q_pos - 1)):
                        idade = K[real[q_pos]]
                        if min_idade is None or idade < min_idade:
                            min_idade = idade
                output_lines.append(str(min_idade))
    
    print('\n'.join(output_lines))

if __name__ == '__main__':
    main()