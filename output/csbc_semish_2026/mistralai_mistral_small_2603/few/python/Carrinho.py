
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    idx = 0
    N = int(data[idx])
    idx += 1
    D = float(data[idx])
    idx += 1

    batteries = []
    for _ in range(N):
        P = float(data[idx])
        idx += 1
        C = float(data[idx])
        idx += 1
        batteries.append((P, C))

    dp = [float('inf')] * N
    dp[0] = 0.0

    for i in range(1, N):
        for j in range(i):
            distance = batteries[i][0] - batteries[j][0]
            time = distance / batteries[j][1]
            if dp[j] + time < dp[i]:
                dp[i] = dp[j] + time

    last_distance = D - batteries[-1][0]
    last_time = last_distance / batteries[-1][1]
    total_time = dp[-1] + last_time

    print(f"{total_time:.3f}")

if __name__ == "__main__":
    main()
