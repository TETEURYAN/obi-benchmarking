
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return

    M = int(data[0])
    N = int(data[1])
    grid = data[2:2+M]

    count = 0
    for i in range(M):
        for j in range(N):
            if grid[i][j] == '#':
                if (i == 0 or grid[i-1][j] == '.') or \
                   (i == M-1 or grid[i+1][j] == '.') or \
                   (j == 0 or grid[i][j-1] == '.') or \
                   (j == N-1 or grid[i][j+1] == '.'):
                    count += 1
    print(count)

if __name__ == "__main__":
    main()
