
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    board = []
    index = 1
    for i in range(n):
        row = list(map(int, data[index:index+n]))
        index += n
        board.append(row)

    for i in range(1, n):
        for j in range(1, n):
            if board[i][j] == 9:
                cells = [board[i][j-1], board[i-1][j-1], board[i-1][j]]
                white = cells.count(0)
                black = cells.count(1)
                if white > black:
                    board[i][j] = 1
                else:
                    board[i][j] = 0

    print(board[n-1][n-1])

if __name__ == "__main__":
    main()
