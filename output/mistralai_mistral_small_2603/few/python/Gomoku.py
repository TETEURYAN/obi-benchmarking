import sys

def main():
    board = []
    for _ in range(15):
        row = list(map(int, sys.stdin.readline().split()))
        board.append(row)

    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

    for i in range(15):
        for j in range(15):
            if board[i][j] == 0:
                continue
            current = board[i][j]
            for dx, dy in directions:
                count = 1
                x, y = i + dx, j + dy
                while 0 <= x < 15 and 0 <= y < 15 and board[x][y] == current:
                    count += 1
                    x += dx
                    y += dy
                x, y = i - dx, j - dy
                while 0 <= x < 15 and 0 <= y < 15 and board[x][y] == current:
                    count += 1
                    x -= dx
                    y -= dy
                if count >= 5:
                    print(current)
                    return
    print(0)

if __name__ == "__main__":
    main()