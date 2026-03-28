
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    N = int(data[idx]); idx += 1
    board = []
    for _ in range(N):
        row = list(map(int, data[idx:idx+N]))
        idx += N
        board.append(row)
    
    row_sums = [0] * N
    col_sums = [0] * N
    
    for i in range(N):
        for j in range(N):
            row_sums[i] += board[i][j]
            col_sums[j] += board[i][j]
    
    max_weight = 0
    for i in range(N):
        for j in range(N):
            weight = row_sums[i] + col_sums[j] - 2 * board[i][j]
            if weight > max_weight:
                max_weight = weight
    
    print(max_weight)

if __name__ == "__main__":
    main()
