
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    T = int(data[0])
    L = int(data[1])
    O = int(data[2])
    D = int(data[3])
    
    line_terminals = []
    index = 4
    for _ in range(L):
        C = int(data[index])
        terminals = list(map(int, data[index+1:index+1+C]))
        index += 1 + C
        line_terminals.append(terminals)
    
    adj = [[] for _ in range(T + 1)]
    for line in line_terminals:
        for u in line:
            for v in line:
                if u != v:
                    adj[u].append(v)
    
    visited = [-1] * (T + 1)
    q = deque()
    q.append(O)
    visited[O] = 0
    
    while q:
        u = q.popleft()
        if u == D:
            print(visited[u])
            return
        for v in adj[u]:
            if visited[v] == -1:
                visited[v] = visited[u] + 1
                q.append(v)
    
    print(-1)

if __name__ == "__main__":
    main()
