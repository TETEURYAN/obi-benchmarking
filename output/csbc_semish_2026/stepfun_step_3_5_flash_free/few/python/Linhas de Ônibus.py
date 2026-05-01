import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    T = int(next(it))
    L = int(next(it))
    O = int(next(it))
    D = int(next(it))
    
    line_terminals = [set() for _ in range(L+1)]
    terminal_lines = [[] for _ in range(T+1)]
    
    for i in range(1, L+1):
        C = int(next(it))
        for _ in range(C):
            t = int(next(it))
            line_terminals[i].add(t)
            terminal_lines[t].append(i)
    
    source_lines = terminal_lines[O]
    target_set = set(terminal_lines[D])
    
    for linha in source_lines:
        if linha in target_set:
            print(1)
            return
    
    dist = [-1] * (L+1)
    visited_terminals = [False] * (T+1)
    q = deque()
    
    for linha in source_lines:
        dist[linha] = 1
        q.append(linha)
    
    while q:
        linha = q.popleft()
        if linha in target_set:
            print(dist[linha])
            return
        for terminal in line_terminals[linha]:
            if not visited_terminals[terminal]:
                visited_terminals[terminal] = True
                for adj in terminal_lines[terminal]:
                    if dist[adj] == -1:
                        dist[adj] = dist[linha] + 1
                        q.append(adj)
    
    print(-1)

if __name__ == "__main__":
    main()