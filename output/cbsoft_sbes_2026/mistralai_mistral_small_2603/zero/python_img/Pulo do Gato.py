
import sys
from collections import deque

def main():
    C = int(sys.stdin.readline())
    colors = list(map(int, sys.stdin.readline().split()))

    if C == 1:
        print(0)
        return

    visited = [-1] * C
    queue = deque()
    queue.append(0)
    visited[0] = 0

    while queue:
        current = queue.popleft()
        max_jump = min(current + 2, C - 1)

        for next_pos in range(current + 1, max_jump + 1):
            if colors[next_pos] == 1 and visited[next_pos] == -1:
                visited[next_pos] = visited[current] + 1
                queue.append(next_pos)

    print(visited[-1] if visited[-1] != -1 else -1)

if __name__ == "__main__":
    main()
