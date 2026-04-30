
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx])
    idx += 1
    A = int(data[idx])
    idx += 1
    B = int(data[idx])
    idx += 1

    graph = [[] for _ in range(N+1)]
    for _ in range(N-1):
        P = int(data[idx])
        idx += 1
        Q = int(data[idx])
        idx += 1
        graph[P].append(Q)
        graph[Q].append(P)

    if A == B:
        print(0)
        return

    visited = [-1] * (N + 1)
    q = deque()
    q.append(A)
    visited[A] = 0

    while q:
        current = q.popleft()
        for neighbor in graph[current]:
            if visited[neighbor] == -1:
                visited[neighbor] = visited[current] + 1
                q.append(neighbor)
                if neighbor == B:
                    print(visited[neighbor])
                    return

    print(visited[B])

if __name__ == "__main__":
    main()
