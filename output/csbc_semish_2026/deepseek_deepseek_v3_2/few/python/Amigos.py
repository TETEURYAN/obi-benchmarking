import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    N = int(data[0])
    K = int(data[1])
    a = [int(x) for x in data[2:2+N]]
    b = [int(x) for x in data[2+N:2+2*N]]

    top_pos = [i for i, v in enumerate(a) if v == 1]
    bot_pos = [i for i, v in enumerate(b) if v == 1]

    INF = 10**18
    dp_prev = [INF] * (K + 1)
    dp_prev[0] = 0

    for i in range(1, K+1):
        dp_cur = [INF] * (K + 1)
        for j in range(1, K+1):
            dist = abs(top_pos[i-1] - bot_pos[j-1])
            dp_cur[j] = min(dp_cur[j], dp_prev[j] + dist)
            dp_cur[j] = min(dp_cur[j], dp_prev[j-1] + dist)
        dp_prev = dp_cur

    ans = dp_prev[K]
    print(ans)

if __name__ == "__main__":
    solve()