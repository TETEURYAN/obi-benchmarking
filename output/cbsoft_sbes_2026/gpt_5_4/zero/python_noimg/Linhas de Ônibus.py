import sys
from collections import deque

def main():
    input = sys.stdin.readline
    T, L, O, D = map(int, input().split())

    terminal_lines = [[] for _ in range(T + 1)]
    lines = []

    for i in range(L):
        data = list(map(int, input().split()))
        c = data[0]
        stops = data[1:]
        lines.append(stops)
        for t in stops:
            terminal_lines[t].append(i)

    dist = [-1] * L
    q = deque()

    for line in terminal_lines[O]:
        dist[line] = 1
        q.append(line)

    visited_terminal = [False] * (T + 1)

    while q:
        line = q.popleft()

        for t in lines[line]:
            if t == D:
                print(dist[line])
                return
            if visited_terminal[t]:
                continue
            visited_terminal[t] = True
            for nxt in terminal_lines[t]:
                if dist[nxt] == -1:
                    dist[nxt] = dist[line] + 1
                    q.append(nxt)

if __name__ == "__main__":
    main()