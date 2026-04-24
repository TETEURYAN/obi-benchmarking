
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    ptr = 0
    test_num = 1
    while True:
        C = int(data[ptr])
        E = int(data[ptr+1])
        L = int(data[ptr+2])
        P = int(data[ptr+3])
        ptr += 4
        if C == 0 and E == 0 and L == 0 and P == 0:
            break

        adj = [[] for _ in range(C + 1)]
        for _ in range(E):
            X = int(data[ptr])
            Y = int(data[ptr+1])
            adj[X].append(Y)
            adj[Y].append(X)
            ptr += 2

        visited = [False] * (C + 1)
        queue = deque()
        queue.append((L, 0))
        visited[L] = True
        reachable = []

        while queue:
            city, tolls = queue.popleft()
            if tolls > P:
                continue
            for neighbor in adj[city]:
                if not visited[neighbor] and tolls + 1 <= P:
                    visited[neighbor] = True
                    reachable.append(neighbor)
                    queue.append((neighbor, tolls + 1))

        reachable_sorted = sorted(reachable)
        print(f"Teste {test_num}")
        if reachable_sorted:
            print(' '.join(map(str, reachable_sorted)))
        else:
            print()
        print()
        test_num += 1

if __name__ == "__main__":
    main()
