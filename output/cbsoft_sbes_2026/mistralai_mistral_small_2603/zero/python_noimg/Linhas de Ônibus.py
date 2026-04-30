
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    ptr = 0
    T = int(data[ptr]); ptr += 1
    L = int(data[ptr]); ptr += 1
    O = int(data[ptr]); ptr += 1
    D = int(data[ptr]); ptr += 1

    lines = []
    for _ in range(L):
        C = int(data[ptr]); ptr += 1
        terminals = list(map(int, data[ptr:ptr+C]))
        ptr += C
        lines.append(set(terminals))

    if O == D:
        print(0)
        return

    line_for_terminal = {}
    for line_idx, terminals in enumerate(lines):
        for t in terminals:
            if t not in line_for_terminal:
                line_for_terminal[t] = []
            line_for_terminal[t].append(line_idx)

    visited_lines = [-1] * L
    queue = deque()
    for line_idx in line_for_terminal.get(O, []):
        visited_lines[line_idx] = 1
        queue.append(line_idx)

    while queue:
        current_line = queue.popleft()
        for t in lines[current_line]:
            if t == D:
                print(visited_lines[current_line])
                return
            for next_line in line_for_terminal.get(t, []):
                if visited_lines[next_line] == -1:
                    visited_lines[next_line] = visited_lines[current_line] + 1
                    queue.append(next_line)

    print(-1)

if __name__ == "__main__":
    main()
