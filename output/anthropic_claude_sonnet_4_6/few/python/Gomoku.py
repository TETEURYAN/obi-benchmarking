import sys

data = sys.stdin.read().split()
board = []
idx = 0
for i in range(15):
    row = []
    for j in range(15):
        row.append(int(data[idx]))
        idx += 1
    board.append(row)

def check_winner(player):
    directions = [(0,1),(1,0),(1,1),(1,-1)]
    for r in range(15):
        for c in range(15):
            if board[r][c] == player:
                for dr, dc in directions:
                    count = 1
                    nr, nc = r+dr, c+dc
                    while 0 <= nr < 15 and 0 <= nc < 15 and board[nr][nc] == player:
                        count += 1
                        nr += dr
                        nc += dc
                    if count >= 5:
                        return True
    return False

if check_winner(1):
    print(1)
elif check_winner(2):
    print(2)
else:
    print(0)