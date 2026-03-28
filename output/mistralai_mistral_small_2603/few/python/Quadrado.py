
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    N = int(data[0])
    if N == 1:
        print(1)
        return
    if N == 2:
        print(-1)
        return
    if N == 3:
        print("1 2 3")
        print("4 5 6")
        print("7 8 9")
        return
    if N == 4:
        print("1 2 3 6")
        print("7 8 9 12")
        print("13 14 15 18")
        print("31 32 33 36")
        return

    square = [[0] * N for _ in range(N)]
    current = 1
    for i in range(N):
        for j in range(N):
            square[i][j] = current
            current += 1

    for i in range(N):
        square[i][N-1] = square[i][N-2] + 3

    for i in range(N-1):
        square[N-1][i] = square[N-2][i] + 18

    for row in square:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()
