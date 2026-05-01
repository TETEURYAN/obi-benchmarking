
def main():
    A = int(input())
    B = int(input())

    if A == 0 and B == 0:
        print(-1, -1)
        return

    if A == 0:
        print(-1, -1)
        return

    if B == 0:
        print(-1, -1)
        return

    if A < 4:
        print(-1, -1)
        return

    if B < 1:
        print(-1, -1)
        return

    if (A - 4) % 4 != 0:
        print(-1, -1)
        return

    k = (A - 4) // 4
    if k < 0:
        print(-1, -1)
        return

    n = k + 2
    m = k + 2

    if n * m - k * k != B:
        print(-1, -1)
        return

    if n > m:
        n, m = m, n

    print(n, m)

if __name__ == "__main__":
    main()
