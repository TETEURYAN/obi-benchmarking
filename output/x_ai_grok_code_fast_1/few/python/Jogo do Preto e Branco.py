import sys

input_data = sys.stdin.read().split()
L = int(input_data[0])
C = int(input_data[1])
P = int(input_data[2])
board = [[0 for _ in range(C)] for _ in range(L)]
idx = 3
for _ in range(P):
    x = int(input_data[idx]) - 1
    y = int(input_data[idx + 1]) - 1
    board[x][y] = 1
    idx += 2

candidatas = []
for i in range(L):
    for j in range(C):
        if board[i][j] == 0:
            has_black = False
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < L and 0 <= nj < C and board[ni][nj] == 1:
                    has_black = True
                    break
            if has_black:
                candidatas.append((i, j))

max_count = 0

def backtrack(index):
    global max_count
    if index == len(candidatas):
        count = 0
        for i, j in candidatas:
            if board[i][j] == 2:
                count += 1
        max_count = max(max_count, count)
        return
    pos = candidatas[index]
    i, j = pos
    # não colocar
    backtrack(index + 1)
    # tentar colocar
    can = True
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < L and 0 <= nj < C and board[ni][nj] == 2:
            can = False
            break
    if can:
        board[i][j] = 2
        backtrack(index + 1)
        board[i][j] = 0

backtrack(0)
print(max_count)