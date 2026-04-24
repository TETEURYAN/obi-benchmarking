import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    L = int(next(it))
    H = int(next(it))
    S = [int(next(it)) for _ in range(N)]
    M = [int(next(it)) for _ in range(N)]
    
    INF_NEG = -10**15
    dp = [INF_NEG] * (H + 1)
    dp[0] = 0
    
    res = INF_NEG
    if L == 0:
        res = 0
    
    for i in range(N):
        s = S[i]
        m = M[i]
        new_dp = [INF_NEG] * (H + 1)
        if m <= H:
            if s > new_dp[m]:
                new_dp[m] = s
        for k in range(H + 1):
            if dp[k] != INF_NEG:
                nk = k + m
                if nk <= H:
                    val = dp[k] + s
                    if val > new_dp[nk]:
                        new_dp[nk] = val
        for k in range(L, H + 1):
            if new_dp[k] > res:
                res = new_dp[k]
        dp = new_dp
    
    print(res)

if __name__ == "__main__":
    main()