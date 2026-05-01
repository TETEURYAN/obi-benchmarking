import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    T = int(input_data[0])
    L = int(input_data[1])
    O = int(input_data[2])
    D = int(input_data[3])
    
    lines = []
    terminals_to_lines = [[] for _ in range(T + 1)]
    
    idx = 4
    for i in range(L):
        C = int(input_data[idx])
        idx += 1
        current_line_terminals = []
        for _ in range(C):
            t = int(input_data[idx])
            idx += 1
            current_line_terminals.append(t)
            terminals_to_lines[t].append(i)
        lines.append(current_line_terminals)
        
    dist = [-1] * (T + 1)
    dist[O] = 0
    
    queue = deque([O])
    visited_lines = [False] * L
    
    while queue:
        curr_t = queue.popleft()
        
        for l in terminals_to_lines[curr_t]:
            if not visited_lines[l]:
                visited_lines[l] = True
                for nxt_t in lines[l]:
                    if dist[nxt_t] == -1:
                        dist[nxt_t] = dist[curr_t] + 1
                        if nxt_t == D:
                            print(dist[D])
                            return
                        queue.append(nxt_t)

if __name__ == '__main__':
    solve()