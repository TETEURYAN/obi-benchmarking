
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    idx = 0
    N = int(data[idx])
    idx += 1

    M1 = int(data[idx])
    idx += 1
    A = list(map(int, data[idx:idx + M1]))
    idx += M1

    M2 = int(data[idx])
    idx += 1
    B = list(map(int, data[idx:idx + M2]))
    idx += M2

    dp = [[-10**18] * (M2 + 1) for _ in range(M1 + 1)]
    dp[0][0] = 0

    for i in range(M1 + 1):
        for j in range(M2 + 1):
            if i < M1 and j < M2:
                current = dp[i][j]
                if current != -10**18:
                    dp[i + 1][j + 1] = max(dp[i + 1][j + 1], current + A[i] * B[j])
            if i < M1:
                current = dp[i][j]
                if current != -10**18:
                    dp[i + 1][j] = max(dp[i + 1][j], current)
            if j < M2:
                current = dp[i][j]
                if current != -10**18:
                    dp[i][j + 1] = max(dp[i][j + 1], current)

    print(dp[M1][M2])

if __name__ == "__main__":
    main()
