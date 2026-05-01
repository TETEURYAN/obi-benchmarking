
def main():
    import sys
    N, T = map(int, sys.stdin.readline().split())
    if T == 0:
        print(N)
    elif T == 1:
        print(N * (N - 1))
    else:
        total = 0
        for k in range(1, N - 1):
            total += (k) * (N - k - 1)
        print(total)

if __name__ == "__main__":
    main()
