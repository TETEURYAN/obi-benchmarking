import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    N, K = data[0], data[1]
    a = data[2:2 + N]
    b = data[2 + N:2 + 2 * N]

    pos_a = []
    pos_b = []

    for i, x in enumerate(a, 1):
        if x == 1:
            pos_a.append(i)
    for i, x in enumerate(b, 1):
        if x == 1:
            pos_b.append(i)

    diff = [0] * K
    for i in range(K):
        diff[i] = pos_a[i] - pos_b[i]

    diff.sort()
    median = diff[K // 2]

    ans = 0
    for d in diff:
        ans += abs(d - median)

    print(ans)

if __name__ == "__main__":
    main()
