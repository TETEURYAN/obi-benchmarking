import sys
from collections import deque

def main():
    input = sys.stdin.readline
    T, L, O, D = map(int, input().split())

    terminal_to_lines = [[] for _ in range(T + 1)]
    lines = []

    for i in range(L):
        data = list(map(int, input().split()))
        c = data[0]
        stops = data[1:]
        lines.append(stops)
        for t in stops:
            terminal_to_lines[t].append(i)

    dist = [-1] * L
    q = deque()

    for line in terminal_to_lines[O]:
        dist[line] = 1
        q.append(line)

    while q:
        line = q.popleft()

        for terminal in lines[line]:
            if terminal == D:
                print(dist[line])
                return
            for nxt in terminal_to_lines[terminal]:
                if dist[nxt] == -1:
                    dist[nxt] = dist[line] + 1
                    q.append(nxt)
            terminal_to_lines[terminal].clear()

    print(0)

if __name__ == "__main__":
    main()
