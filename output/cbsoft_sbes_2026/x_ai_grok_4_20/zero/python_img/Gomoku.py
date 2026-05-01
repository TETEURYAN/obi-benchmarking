
import sys

board = []
for _ in range(15):
    line = list(map(int, input().split()))
    board.append(line)

directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

def check_win(player):
    for i in range(15):
        for j in range(15):
            if board[i][j] != player:
                continue
            for di, dj in directions:
                count = 1
                ni, nj = i + di, j + dj
                while 0 <= ni < 15 and 0 <= nj < 15 and board[ni][nj] == player:
                    count += 1
                    ni += di
                    nj += dj
                if count >= 5:
                    return True
    return False

if check_win(1):
    print(1)
elif check_win(2):
    print(2)
else:
    print(0)
