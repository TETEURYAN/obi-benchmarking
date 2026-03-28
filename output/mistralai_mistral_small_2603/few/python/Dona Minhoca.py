
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    k = int(next(it))
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    if k == 1:
        print(n - 1)
        return

    def bfs(start):
        dist = [-1] * (n + 1)
        q = deque()
        q.append(start)
        dist[start] = 0
        while q:
            u = q.popleft()
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
        return dist

    dist1 = bfs(1)
    u = dist1.index(max(dist1))
    dist_u = bfs(u)
    v = dist_u.index(max(dist_u))
    diameter = max(dist_u)

    def check(R):
        visited = [False] * (n + 1)
        count = 0
        q = deque()
        for i in range(1, n + 1):
            if not visited[i]:
                count += 1
                if count > k:
                    return False
                q.append(i)
                visited[i] = True
                while q:
                    node = q.popleft()
                    for neighbor in adj[node]:
                        if not visited[neighbor] and dist_u[node] <= R and dist_u[neighbor] <= R:
                            visited[neighbor] = True
                            q.append(neighbor)
        return count <= k

    low = 0
    high = diameter
    answer = high
    while low <= high:
        mid = (low + high) // 2
        if check(mid):
            answer = mid
            high = mid - 1
        else:
            low = mid + 1
    print(answer)

if __name__ == "__main__":
    main()
