import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    idx = 0
    T = int(data[idx]); idx+=1
    L = int(data[idx]); idx+=1
    O = int(data[idx]); idx+=1
    D = int(data[idx]); idx+=1
    
    lines = []
    for i in range(L):
        c = int(data[idx]); idx+=1
        terminals = []
        for j in range(c):
            terminals.append(int(data[idx])); idx+=1
        lines.append(terminals)
    
    # terminal_to_lines[t] = list of line indices passing through terminal t
    terminal_to_lines = [[] for _ in range(T+1)]
    for i, line in enumerate(lines):
        for t in line:
            terminal_to_lines[t].append(i)
    
    # BFS on lines
    # We want minimum number of lines used to get from O to D
    # dist[line] = number of lines used when we first board this line
    
    # Start: find all lines containing O
    # BFS: state = line index, cost = number of lines used
    
    INF = float('inf')
    dist_line = [INF] * L
    
    queue = deque()
    
    # Initialize: all lines containing O get distance 1
    for line_idx in terminal_to_lines[O]:
        if dist_line[line_idx] == INF:
            dist_line[line_idx] = 1
            queue.append(line_idx)
    
    # Check if D is reachable from any initial line
    # BFS
    visited_terminal = [False] * (T+1)
    visited_terminal[O] = True
    
    # We also need to track which terminals have been "expanded"
    # When we process a line, we look at all terminals in that line
    # For each terminal not yet visited, we add all lines through that terminal
    
    visited_line = [False] * L
    
    # Re-do BFS properly
    dist_line = [INF] * L
    visited_terminal = [False] * (T+1)
    visited_terminal[O] = True
    
    queue = deque()
    for line_idx in terminal_to_lines[O]:
        if dist_line[line_idx] == INF:
            dist_line[line_idx] = 1
            queue.append(line_idx)
    
    ans = INF
    
    while queue:
        line_idx = queue.popleft()
        d = dist_line[line_idx]
        
        # Check if D is in this line
        if D in set(lines[line_idx]):
            ans = min(ans, d)
            continue
        
        # Expand all terminals in this line
        for t in lines[line_idx]:
            if not visited_terminal[t]:
                visited_terminal[t] = True
                for next_line in terminal_to_lines[t]:
                    if dist_line[next_line] == INF:
                        dist_line[next_line] = d + 1
                        queue.append(next_line)
    
    print(ans)

solve()