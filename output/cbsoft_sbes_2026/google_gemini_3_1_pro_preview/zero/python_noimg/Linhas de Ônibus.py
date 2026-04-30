import sys
from collections import deque

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    T = int(input_data[0])
    L = int(input_data[1])
    O = int(input_data[2])
    D = int(input_data[3])
    
    lines_of_terminal = [[] for _ in range(T + 1)]
    terminals_of_line = [[] for _ in range(L + 1)]
    
    idx = 4
    for i in range(1, L + 1):
        C = int(input_data[idx])
        idx += 1
        for _ in range(C):
            t = int(input_data[idx])
            idx += 1
            terminals_of_line[i].append(t)
            lines_of_terminal[t].append(i)
            
    visited_terminals = [False] * (T + 1)
    visited_lines = [False] * (L + 1)
    
    queue = deque()
    
    visited_terminals[O] = True
    for line in lines_of_terminal[O]:
        visited_lines[line] = True
        queue.append((line, 1))
        
    while queue:
        curr_line, dist = queue.popleft()
        
        for t in terminals_of_line[curr_line]:
            if t == D:
                print(dist)
                return
            if not visited_terminals[t]:
                visited_terminals[t] = True
                for nxt_line in lines_of_terminal[t]:
                    if not visited_lines[nxt_line]:
                        visited_lines[nxt_line] = True
                        queue.append((nxt_line, dist + 1))

if __name__ == '__main__':
    main()