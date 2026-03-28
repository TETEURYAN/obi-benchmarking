import sys

lines = sys.stdin.read().split()
board = []
for line in lines:
    board.append(line)

count = 0
directions = [(-1,0),(1,0),(0,-1),(0,1)]

for r in range(7):
    for c in range(7):
        if board[r][c] == 'o':
            for dr, dc in directions:
                tr, tc = r+dr, c+dc
                dr2, dc2 = r+2*dr, c+2*dc
                if 0 <= tr < 7 and 0 <= tc < 7 and 0 <= dr2 < 7 and 0 <= dc2 < 7:
                    if board[tr][tc] == 'o' and board[dr2][dc2] == '.':
                        if board[tr][tc] != '-' and board[dr2][dc2] != '-':
                            count += 1

print(count)