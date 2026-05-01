
def main():
    A = int(input())
    B = int(input())

    if A == 0 and B == 0:
        print(-1, -1)
        return

    if A < 4:
        print(-1, -1)
        return

    if (A - 4) % 4 != 0:
        print(-1, -1)
        return

    n = (A - 4) // 4
    if n < 0:
        print(-1, -1)
        return

    total = B + A
    if n == 0:
        if total != 1:
            print(-1, -1)
            return
        else:
            print(1, 1)
            return

    k = n + 2
    if k * k != total:
        print(-1, -1)
        return

    print(min(k, k), max(k, k))

if __name__ == "__main__":
    main()
