import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    m, n = data[0], data[1]
    saldo = [0] * (n + 1)
    total = 0

    idx = 2
    for _ in range(m):
        x = data[idx]
        v = data[idx + 1]
        y = data[idx + 2]
        idx += 3
        saldo[x] -= v
        saldo[y] += v
        total += v

    minimo = 0
    for i in range(1, n + 1):
        if saldo[i] > 0:
            minimo += saldo[i]

    sys.stdout.write(("S\n" if minimo < total else "N\n") + str(minimo) + "\n")

if __name__ == "__main__":
    main()
