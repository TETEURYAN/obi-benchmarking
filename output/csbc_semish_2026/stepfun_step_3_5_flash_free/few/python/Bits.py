import sys

MOD = 10**9 + 7

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    N = int(data[0])
    K = int(data[1])
    if K > N:
        print(pow(2, N, MOD))
        return
    dp_prev = [0] * K
    dp_prev[0] = 1
    for i in range(1, N + 1):
        total = sum(dp_prev) % MOD
        dp_curr = [0] * K
        dp_curr[0] = total
        for j in range(1, K):
            dp_curr[j] = dp_prev[j - 1]
        dp_prev = dp_curr
    ans = sum(dp_prev) % MOD
    print(ans)

if __name__ == "__main__":
    main()