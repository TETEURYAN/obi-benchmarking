
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
index = 1
board = []
for i in range(N):
    row = []
    for j in range(N):
        row.append(int(data[index]))
        index += 1
    board.append(row)

for i in range(1, N):
    for j in range(1, N):
        a = board[i][j-1]
        b = board[i-1][j-1]
        c = board[i-1][j]
        whites = (a == 0) + (b == 0) + (c == 0)
        blacks = 3 - whites
        if whites > blacks:
            board[i][j] = 1
        else:
            board[i][j] = 0

print(board[N-1][N-1])
