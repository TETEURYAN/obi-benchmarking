
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    ptr = 0
    X = int(data[ptr])
    ptr += 1
    Y = int(data[ptr])
    ptr += 1
    N = int(data[ptr])
    ptr += 1
    A = int(data[ptr])
    ptr += 1

    cities = []
    for _ in range(N):
        xi = int(data[ptr])
        ptr += 1
        yi = int(data[ptr])
        ptr += 1
        cities.append((xi, yi))

    adj = [[] for _ in range(N+1)]
    for i in range(N):
        xi, yi = cities[i]
        for j in range(i+1, N):
            xj, yj = cities[j]
            dist = abs(xi - xj) + abs(yi - yj)
            if dist <= A:
                adj[i+1].append(j+1)
                adj[j+1].append(i+1)

    visited = [False] * (N+1)
    plane_trips = 0
    queue = deque()
    queue.append(1)
    visited[1] = True

    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)

    for i in range(1, N+1):
        if not visited[i]:
            plane_trips += 1

    print(plane_trips)

if __name__ == "__main__":
    main()
