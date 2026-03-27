
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print(-1)
        return

    ptr = 0
    V = int(data[ptr])
    ptr += 1
    N = int(data[ptr])
    ptr += 1
    M = int(data[ptr])
    ptr += 1

    adj = [[] for _ in range(N + 1)]
    for _ in range(M):
        a = int(data[ptr])
        b = int(data[ptr + 1])
        t = int(data[ptr + 2])
        p = int(data[ptr + 3])
        ptr += 4
        adj[a].append((b, t, p))
        adj[b].append((a, t, p))

    X = int(data[ptr])
    ptr += 1
    Y = int(data[ptr])
    ptr += 1

    INF = float('inf')
    max_p = V
    dp = [[INF] * (max_p + 1) for _ in range(N + 1)]
    dp[X][0] = 0

    for p in range(max_p + 1):
        for u in range(1, N + 1):
            if dp[u][p] == INF:
                continue
            for (v, t, cost) in adj[u]:
                new_p = p + cost
                if new_p > max_p:
                    continue
                if dp[v][new_p] > dp[u][p] + t:
                    dp[v][new_p] = dp[u][p] + t

    min_time = INF
    for p in range(max_p + 1):
        if dp[Y][p] < min_time:
            min_time = dp[Y][p]

    if min_time == INF:
        print(-1)
    else:
        print(min_time)

if __name__ == "__main__":
    main()
