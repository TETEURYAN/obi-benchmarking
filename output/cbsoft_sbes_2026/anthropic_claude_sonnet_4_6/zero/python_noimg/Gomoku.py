board = []
for _ in range(15):
    row = list(map(int, input().split()))
    board.append(row)

def check_winner(player):
    directions = [(0,1),(1,0),(1,1),(1,-1)]
    for i in range(15):
        for j in range(15):
            if board[i][j] == player:
                for di, dj in directions:
                    count = 1
                    ni, nj = i+di, j+dj
                    while 0 <= ni < 15 and 0 <= nj < 15 and board[ni][nj] == player:
                        count += 1
                        ni += di
                        nj += dj
                    if count >= 5:
                        return True
    return False

if check_winner(1):
    print(1)
elif check_winner(2):
    print(2)
else:
    print(0)