from collections import deque

def solve():
    import sys
    input_data = sys.stdin.read().split()
    idx = 0
    
    T = int(input_data[idx]); idx += 1
    L = int(input_data[idx]); idx += 1
    O = int(input_data[idx]); idx += 1
    D = int(input_data[idx]); idx += 1
    
    lines = []
    terminal_to_lines = [[] for _ in range(T + 1)]
    
    for i in range(L):
        C = int(input_data[idx]); idx += 1
        terminals = []
        for j in range(C):
            t = int(input_data[idx]); idx += 1
            terminals.append(t)
        lines.append(terminals)
        for t in terminals:
            terminal_to_lines[t].append(i)
    
    # BFS on lines
    # We want minimum number of lines used
    # State: current set of reachable terminals
    # Better: BFS where nodes are bus lines
    # dist[line] = minimum lines used to reach any terminal in that line from O
    
    # First, find which lines contain O
    # Then BFS expanding lines
    
    INF = float('inf')
    line_dist = [INF] * L
    
    queue = deque()
    
    # Lines containing origin terminal O
    for line_idx in terminal_to_lines[O]:
        if line_dist[line_idx] == INF:
            line_dist[line_idx] = 1
            queue.append(line_idx)
    
    # Check if D is reachable from O directly
    # BFS over lines
    visited_lines = set()
    for line_idx in terminal_to_lines[O]:
        visited_lines.add(line_idx)
    
    # visited terminals (to avoid re-processing)
    visited_terminals = set()
    visited_terminals.add(O)
    
    # Add all terminals of initial lines to frontier
    # Actually let's do proper BFS
    
    # Reset and redo properly
    line_dist = [INF] * L
    visited_lines = [False] * L
    visited_terminals = [False] * (T + 1)
    
    visited_terminals[O] = True
    
    queue = deque()
    
    for line_idx in terminal_to_lines[O]:
        if not visited_lines[line_idx]:
            visited_lines[line_idx] = True
            line_dist[line_idx] = 1
            queue.append(line_idx)
    
    ans = INF
    
    while queue:
        line_idx = queue.popleft()
        d = line_dist[line_idx]
        
        # Check if destination is in this line
        for t in lines[line_idx]:
            if t == D:
                ans = min(ans, d)
                break
        
        # Expand: for each terminal in this line, find connected lines
        for t in lines[line_idx]:
            if not visited_terminals[t]:
                visited_terminals[t] = True
                for next_line in terminal_to_lines[t]:
                    if not visited_lines[next_line]:
                        visited_lines[next_line] = True
                        line_dist[next_line] = d + 1
                        queue.append(next_line)
    
    print(ans)

solve()