import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[0], data[1]
    bar = data[2:2 + n]
    seq = data[2 + n:2 + n + m]

    diff = [0] * (n + 2)

    for i in range(m - 1):
        a = seq[i]
        b = seq[i + 1]
        l = min(a, b)
        r = max(a, b)
        diff[l] += 1
        diff[r + 1] -= 1

    counts = [0] * 10
    cur = 0
    for i in range(1, n + 1):
        cur += diff[i]
        counts[bar[i - 1]] += cur

    counts[bar[seq[0] - 1]] += 1

    print(*counts)

if __name__ == "__main__":
    main()
