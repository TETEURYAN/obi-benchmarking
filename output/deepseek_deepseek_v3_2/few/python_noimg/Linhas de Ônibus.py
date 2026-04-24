import sys
sys.setrecursionlimit(200000)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    T = int(next(it))
    L = int(next(it))
    O = int(next(it))
    D = int(next(it))
    
    terminal_to_lines = [[] for _ in range(T + 1)]
    for line_id in range(1, L + 1):
        C = int(next(it))
        for _ in range(C):
            terminal = int(next(it))
            terminal_to_lines[terminal].append(line_id)
    
    from collections import deque
    INF = 10**9
    dist_line = [INF] * (L + 1)
    q = deque()
    for line in terminal_to_lines[O]:
        dist_line[line] = 1
        q.append(line)
    
    visited_terminal = [False] * (T + 1)
    visited_terminal[O] = True
    
    while q:
        line = q.popleft()
        C = int(data[4 + (line - 1) * 2])
        start_idx = 5 + (line - 1) * 2
        for i in range(C):
            terminal = int(data[start_idx + i])
            if terminal == D:
                print(dist_line[line])
                return
            if not visited_terminal[terminal]:
                visited_terminal[terminal] = True
                for next_line in terminal_to_lines[terminal]:
                    if dist_line[next_line] == INF:
                        dist_line[next_line] = dist_line[line] + 1
                        q.append(next_line)
    
    print(-1)

if __name__ == "__main__":
    solve()