import sys

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    
    col_sums = [0] * M
    total = 0
    
    for _ in range(N):
        row = list(map(int, input().split()))
        for j, v in enumerate(row):
            col_sums[j] += v
            total += v
    
    prefix = 0
    ans = total
    
    for j in range(M - 1):
        prefix += col_sums[j]
        cost = min(prefix, total - prefix)
        if cost < ans:
            ans = cost
    
    print(ans)

if __name__ == "__main__":
    main()
