
def main():
    import sys
    N, T = map(int, sys.stdin.readline().split())
    if T == 0:
        print(N)
    elif T == 1:
        print(N * (N - 1) // 2)
    else:
        if N < 3:
            print(0)
            return
        total = 0
        for k in range(1, N - 1):
            total += (k) * (N - 1 - k)
        print(total)

if __name__ == "__main__":
    main()
