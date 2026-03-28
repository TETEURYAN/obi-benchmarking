import sys

def main():
    lines = [sys.stdin.readline().strip() for _ in range(7)]
    count = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for i in range(7):
        for j in range(7):
            if lines[i][j] == 'o':
                for dx, dy in directions:
                    ni = i + dx
                    nj = j + dy
                    ni2 = i + 2 * dx
                    nj2 = j + 2 * dy
                    if 0 <= ni < 7 and 0 <= nj < 7 and 0 <= ni2 < 7 and 0 <= nj2 < 7:
                        if lines[ni][nj] == 'o' and lines[ni2][nj2] == '.':
                            count += 1
    print(count)

if __name__ == "__main__":
    main()