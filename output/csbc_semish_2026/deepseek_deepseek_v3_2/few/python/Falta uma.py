import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    total = 1
    for i in range(2, N + 1):
        total *= i
    expected_sum = [0] * N
    for i in range(total - 1):
        for j in range(N):
            val = int(next(it))
            expected_sum[j] += val
    full_sum = N * (N + 1) // 2
    missing = [full_sum - s for s in expected_sum]
    print(' '.join(map(str, missing)))

if __name__ == "__main__":
    main()