import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    K = int(next(it))
    X = [int(next(it)) for _ in range(N)]
    X.sort()
    window_size = N - K
    ans = float('inf')
    for i in range(N - window_size + 1):
        ans = min(ans, X[i + window_size - 1] - X[i])
    print(ans)

if __name__ == "__main__":
    main()