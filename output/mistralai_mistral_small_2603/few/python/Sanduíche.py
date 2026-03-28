
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return

    n = int(data[0])
    m = int(data[1])

    if m == 0:
        print((1 << n) - 1)
        return

    forbidden = [0] * (n + 1)
    idx = 2
    for _ in range(m):
        x = int(data[idx])
        y = int(data[idx + 1])
        forbidden[x] |= (1 << (y - 1))
        forbidden[y] |= (1 << (x - 1))
        idx += 2

    total = 0
    for mask in range(1, 1 << n):
        valid = True
        for i in range(n):
            if (mask & (1 << i)) == 0:
                continue
            if (mask & forbidden[i + 1]) != 0:
                valid = False
                break
        if valid:
            total += 1

    print(total)

if __name__ == "__main__":
    main()
