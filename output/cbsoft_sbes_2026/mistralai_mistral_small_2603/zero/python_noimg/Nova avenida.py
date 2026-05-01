
import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx])
    M = int(data[idx+1])
    idx += 2

    grid = []
    for _ in range(N):
        row = list(map(int, data[idx:idx+M]))
        grid.append(row)
        idx += M

    min_sum = float('inf')
    for j in range(M):
        current_sum = 0
        for i in range(N):
            current_sum += grid[i][j]
        if current_sum < min_sum:
            min_sum = current_sum

    print(min_sum)

if __name__ == "__main__":
    main()
