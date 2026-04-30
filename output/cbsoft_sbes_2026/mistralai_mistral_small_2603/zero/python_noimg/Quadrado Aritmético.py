
def main():
    import sys
    data = sys.stdin.read().split()
    N = int(data[0])
    S = int(data[1])

    if N == 1:
        print(S)
        return

    base = S // N
    remainder = S % N

    matrix = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i == j:
                matrix[i][j] = base + remainder
            else:
                matrix[i][j] = base

    for row in matrix:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()
