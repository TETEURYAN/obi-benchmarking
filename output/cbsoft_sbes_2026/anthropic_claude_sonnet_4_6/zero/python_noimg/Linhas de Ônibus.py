from collections import deque
import sys
input = sys.stdin.readline

def solve():
    T, L, O, D = map(int, input().split())
    
    lines = []
    terminal_to_lines = [[] for _ in range(T + 1)]
    
    for i in range(L):
        parts = list(map(int, input().split()))
        c = parts[0]
        terminals = parts[1:c+1]
        lines.append(terminals)
        for t in terminals:
            terminal_to_lines[t].append(i)
    
    # BFS on lines
    # We want minimum number of lines to use
    # State: current set of reachable terminals
    # BFS level = number of lines used
    
    if O == D:
        print(0)
        return
    
    # BFS where nodes are bus lines
    # Start: find all lines containing O
    # From a line, we can reach all its terminals
    # From those terminals, we can take other lines
    
    visited_lines = [False] * L
    visited_terminals = [False] * (T + 1)
    
    queue = deque()
    
    visited_terminals[O] = True
    
    # Initialize with lines from O
    for line_idx in terminal_to_lines[O]:
        if not visited_lines[line_idx]:
            visited_lines[line_idx] = True
            queue.append((line_idx, 1))
    
    while queue:
        line_idx, num_lines = queue.popleft()
        
        # Visit all terminals in this line
        new_terminals = []
        for t in lines[line_idx]:
            if not visited_terminals[t]:
                visited_terminals[t] = True
                new_terminals.append(t)
                if t == D:
                    print(num_lines)
                    return
        
        # From new terminals, add new lines
        for t in new_terminals:
            for next_line in terminal_to_lines[t]:
                if not visited_lines[next_line]:
                    visited_lines[next_line] = True
                    queue.append((next_line, num_lines + 1))
    
    print(-1)

solve()