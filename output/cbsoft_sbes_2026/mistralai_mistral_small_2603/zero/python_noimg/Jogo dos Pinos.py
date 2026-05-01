
def main():
    board = [input().strip() for _ in range(7)]
    count = 0

    for i in range(7):
        for j in range(7):
            if board[i][j] == 'o':
                # Check directions: up, down, left, right
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < 7 and 0 <= nj < 7 and board[ni][nj] == 'o':
                        target_i, target_j = ni + di, nj + dj
                        if 0 <= target_i < 7 and 0 <= target_j < 7 and board[target_i][target_j] == '.':
                            count += 1
    print(count)

if __name__ == "__main__":
    main()
