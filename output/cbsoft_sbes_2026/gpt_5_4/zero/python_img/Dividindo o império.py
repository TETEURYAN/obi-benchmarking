import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    parent = [0] * (n + 1)
    order = []
    stack = [1]
    parent[1] = -1

    while stack:
        u = stack.pop()
        order.append(u)
        for v in adj[u]:
            if v != parent[u]:
                parent[v] = u
                stack.append(v)

    size = [1] * (n + 1)
    ans = n

    for u in reversed(order):
        for v in adj[u]:
            if v != parent[u]:
                size[u] += size[v]
        if u != 1:
            diff = abs(n - 2 * size[u])
            if diff < ans:
                ans = diff

    print(ans)

if __name__ == "__main__":
    main()
