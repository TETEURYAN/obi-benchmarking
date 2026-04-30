n = int(input())
board = []
for _ in range(n):
    row = list(map(int, input().split()))
    board.append(row)

for i in range(1, n):
    for j in range(1, n):
        cells = [board[i][j-1], board[i-1][j-1], board[i-1][j]]
        whites = cells.count(0)
        blacks = cells.count(1)
        if whites > blacks:
            board[i][j] = 1
        else:
            board[i][j] = 0

print(board[n-1][n-1])