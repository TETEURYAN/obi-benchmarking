import sys

sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        N = int(next(iterator))
        M = int(next(iterator))
    except StopIteration:
        return

    adj = [[] for _ in range(N + 1)]

    for _ in range(M):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)

    removed = [False] * (N + 1)
    result = []

    for i in range(N, 0, -1):
        if not removed[i]:
            result.append(i)
            for neighbor in adj[i]:
                removed[neighbor] = True

    result.sort()
    
    print(len(result))
    print(*result)

if __name__ == "__main__":
    solve()