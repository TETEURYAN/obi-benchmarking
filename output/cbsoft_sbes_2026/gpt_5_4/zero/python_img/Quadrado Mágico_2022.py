import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    a = []
    zr = zc = -1

    for i in range(n):
        row = list(map(int, input().split()))
        for j, v in enumerate(row):
            if v == 0:
                zr, zc = i, j
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