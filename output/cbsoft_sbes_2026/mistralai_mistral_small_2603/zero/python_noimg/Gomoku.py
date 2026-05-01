
def check_win(board, player):
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == player:
                # Check horizontal
                if j + 4 < n and all(board[i][j+k] == player for k in range(5)):
                    return True
                # Check vertical
                if i + 4 < n and all(board[i+k][j] == player for k in range(5)):
                    return True
                # Check diagonal down-right
                if i + 4 < n and j + 4 < n and all(board[i+k][j+k] == player for k in range(5)):
                    return True
                # Check diagonal down-left
                if i + 4 < n and j - 4 >= 0 and all(board[i+k][j-k] == player for k in range(5)):
                    return True
    return False

def main():
    board = []
    for _ in range(15):
        row = list(map(int, input().split()))
        board.append(row)

    if check_win(board, 1):
        print(1)
    elif check_win(board, 2):
        print(2)
    else:
        print(0)

if __name__ == "__main__":
    main()
