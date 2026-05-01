import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    F = float(next(it))
    X = [int(next(it)) for _ in range(N)]
    
    if N == 1:
        print("0.00")
        return
        
    Y = X + X
    n2 = len(Y)
    P = [0] * (n2 + 1)
    for i in range(n2):
        P[i+1] = P[i] + Y[i]
    
    dp = [[0.0] * n2 for _ in range(n2)]
    
    for L in range(2, N+1):
        for i in range(0, n2 - L + 1):
            j = i + L - 1
            best = float('inf')
            for k in range(i, j):
                soma_esq = P[k+1] - P[i]
                soma_dir = P[j+1] - P[k+1]
                custo = F * max(soma_esq, soma_dir)
                total = custo + dp[i][k] + dp[k+1][j]
                if total < best:
                    best = total
            dp[i][j] = best
    
    ans = float('inf')
    for i in range(N):
        j = i + N - 1
        if dp[i][j] < ans:
            ans = dp[i][j]
    
    print("{:.2f}".format(ans))

if __name__ == "__main__":
    main()