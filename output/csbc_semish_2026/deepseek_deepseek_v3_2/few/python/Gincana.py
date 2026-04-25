import sys
sys.setrecursionlimit(200000)

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    adj = [[] for _ in range(n+1)]
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2

    visited = [False]*(n+1)
    components = 0

    for i in range(1, n+1):
        if not visited[i]:
            components += 1
            stack = [i]
            visited[i] = True
            while stack:
                node = stack.pop()
                for neighbor in adj[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)

    print(components)

if __name__ == "__main__":
    main()