import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

    for i in range(1, n):
        for j in range(1, n):
            s = board[i][j - 1] + board[i - 1][j - 1] + board[i - 1][j]
            board[i][j] = 1 if s <= 1 else 0

    print(board[n - 1][n - 1])

if __name__ == "__main__":
    main()