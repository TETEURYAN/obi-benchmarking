 sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    a = int(data[1])
    b = int(data[2])

    graph = [[] for _ in range(n+1)]
    index = 3
    for _ in range(n-1):
        p = int(data[index])
        q = int(data[index+1])
        index += 2
        graph[p].append(q)
        graph[q].append(p)

    visited = [False] * (n+1)
    parent = [0] * (n+1)
    q = deque()
    q.append(a)
    visited[a] = True

    while q:
        current = q.popleft()
        if current == b:
            break
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = current
                q.append(neighbor)

    distance = 0
    current = b
    while current != a:
        distance += 1
        current = parent[current]

    print(distance)

if __name__ == "__main__":
    main()
