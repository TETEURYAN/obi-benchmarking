import sys

def main():
    N = int(sys.stdin.readline())
    total = N * N * N
    if N < 2:
        print(0)
        print(0)
        print(0)
        print(total)
        return

    nenhuma = (N - 2) ** 3
    uma = 6 * (N - 2) ** 2
    duas = 12 * (N - 2)
    tres = 8

    print(nenhuma)
    print(uma)
    print(duas)
    print(tres)

if __name__ == "__main__":
    main()