import sys

sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    E = int(input_data[0])
    I = int(input_data[1])
    V_count = int(input_data[2])
    
    adj = [[] for _ in range(E + 1)]
    in_degree = [0] * (E + 1)
    
    idx = 3
    for _ in range(I):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].append(v)
        in_degree[v] += 1
        idx += 2
        
    V = []
    for _ in range(V_count):
        V.append(int(input_data[idx]))
        idx += 1
        
    anc = [0] * (E + 1)
    queue = []
    
    for i in range(1, E + 1):
        if in_degree[i] == 0:
            anc[i] = 1 << i
            queue.append(i)
            
    head = 0
    while head < len(queue):
        u = queue[head]
        head += 1
        
        for v in adj[u]:
            anc[v] |= anc[u]
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
                
    result = []
    for x in range(1, E + 1):
        for v in V:
            if (anc[v] & anc[x]) == anc[v]:
                result.append(x)
                break
                
    print(*(result))

if __name__ == '__main__':
    solve()