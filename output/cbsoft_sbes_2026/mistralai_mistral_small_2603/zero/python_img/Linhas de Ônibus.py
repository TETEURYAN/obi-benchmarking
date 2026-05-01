
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    ptr = 0
    T = int(data[ptr])
    ptr += 1
    L = int(data[ptr])
    ptr += 1
    O = int(data[ptr])
    ptr += 1
    D = int(data[ptr])
    ptr += 1

    lines = []
    for _ in range(L):
        C = int(data[ptr])
        ptr += 1
        terminals = list(map(int, data[ptr:ptr + C]))
        ptr += C
        lines.append(set(terminals))

    # Build adjacency list: terminal -> list of line indices that pass through it
    terminal_to_lines = {}
    for line_idx in range(L):
        for terminal in lines[line_idx]:
            if terminal not in terminal_to_lines:
                terminal_to_lines[terminal] = []
            terminal_to_lines[terminal].append(line_idx)

    # BFS setup: (current_line, number_of_changes)
    visited_lines = [False] * L
    queue = deque()
    # Start from all lines that pass through O
    for line_idx in terminal_to_lines.get(O, []):
        queue.append((line_idx, 0))
        visited_lines[line_idx] = True

    while queue:
        current_line, changes = queue.popleft()
        # Check if this line passes through D
        if D in lines[current_line]:
            print(changes)
            return
        # Explore all terminals in this line
        for terminal in lines[current_line]:
            # For each line passing through this terminal
            for next_line in terminal_to_lines.get(terminal, []):
                if not visited_lines[next_line]:
                    visited_lines[next_line] = True
                    queue.append((next_line, changes + 1))

    # If no path found (shouldn't happen per problem statement)
    print(-1)

if __name__ == "__main__":
    main()
