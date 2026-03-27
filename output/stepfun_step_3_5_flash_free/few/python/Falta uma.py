import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    total = n * (n + 1) // 2
    fat = 1
    for i in range(1, n):
        fat *= i
    expected = fat * total
    sums = [0] * n
    idx = 1
    while idx < len(data):
        for j in range(n):
            sums[j] += int(data[idx])
            idx += 1
    missing = [expected - s for s in sums]
    print(' '.join(map(str, missing)))

if __name__ == "__main__":
    main()