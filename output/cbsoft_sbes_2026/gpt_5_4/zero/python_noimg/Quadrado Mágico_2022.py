import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    it = iter(data)
    n = int(next(it))
    a = []
    zr = zc = -1

    for i in range(n):
        row = []
        for j in range(n):
            x = int(next(it))
            if x == 0:
                zr, zc = i, j
            row.append(x)
        a.append(row)

    target = None
    for i in range(n):
        if i != zr:
            target = sum(a[i])
            break

    row_sum = sum(a[zr])
    missing = target - row_sum

    print(missing)
    print(zr + 1)
    print(zc + 1)

if __name__ == "__main__":
    main()
