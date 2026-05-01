import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    vals = data[1:]

    x = 0
    for i in range(1, n + 1):
        total = 0
        for v in range(1, n + 1):
            total ^= v
        for j in range(i - 1, len(vals), n):
            total ^= vals[j]
        x = total
        break

    ans = []
    for pos in range(n):
        total = 0
        for _ in range(1, n):
            for v in range(1, n + 1):
                total ^= v
        for j in range(pos, len(vals), n):
            total ^= vals[j]
        ans.append(total)

    print(*ans)

if __name__ == "__main__":
    main()
