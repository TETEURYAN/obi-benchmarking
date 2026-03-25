import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    N = int(data[0])
    K = int(data[1])
    dolls = list(map(int, data[2:]))
    dolls.sort()

    # precompute all trio costs for consecutive triples
    trio_costs = []
    for i in range(N - 2):
        a, b, c = dolls[i], dolls[i+1], dolls[i+2]
        trio_costs.append((b - a) ** 2)

    INF = 10**18
    dp_prev = [INF] * (K + 1)
    dp_prev[0] = 0
    dp_cur = [INF] * (K + 1)

    for i in range(N - 2):
        # fill dp_cur
        for k in range(1, K + 1):
            dp_cur[k] = dp_prev[k]
            if i >= 2 and k > 0:
                dp_cur[k] = min(dp_cur[k], dp_prev[k-1] + trio_costs[i])
        # shift
        dp_prev = dp_cur
        dp_cur = [INF] * (K + 1)

    print(dp_prev[K])

if __name__ == "__main__":
    main()