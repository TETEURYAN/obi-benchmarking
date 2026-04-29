import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    n = int(data[0])
    idx = 1

    board = []
    for _ in range(n):
        row = list(map(int, data[idx:idx + n]))
        idx += n
        board.append(row)

    for i in range(1, n):
        for j in range(1, n):
            s = board[i][j - 1] + board[i - 1][j - 1] + board[i - 1][j]
            board[i][j] = 1 if s <= 1 else 0

    print(board[n - 1][n - 1])

if __name__ == "__main__":
    main()
