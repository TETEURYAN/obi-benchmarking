
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    board = []
    index = 1
    for i in range(n):
        row = list(map(int, data[index:index+n]))
        board.append(row)
        index += n

    for i in range(1, n):
        for j in range(1, n):
            if board[i][j] == 9:
                count_white = 0
                count_black = 0
                if board[i][j-1] == 0:
                    count_white += 1
                elif board[i][j-1] == 1:
                    count_black += 1
                if board[i-1][j-1] == 0:
                    count_white += 1
                elif board[i-1][j-1] == 1:
                    count_black += 1
                if board[i-1][j] == 0:
                    count_white += 1
                elif board[i-1][j] == 1:
                    count_black += 1
                if count_white > count_black:
                    board[i][j] = 1
                else:
                    board[i][j] = 0

    print(board[n-1][n-1])

if __name__ == "__main__":
    main()
