import sys

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())

    col_sums = [0] * M
    for _ in range(N):
        row = list(map(int, input().split()))
        for j in range(M):
            col_sums[j] += row[j]

    total = sum(col_sums)
    left = 0
    ans = total

    for j in range(M - 1):
        left += col_sums[j]
        cost = min(left, total - left)
        if cost < ans:
            ans = cost

    print(ans)

if __name__ == "__main__":
    main()
