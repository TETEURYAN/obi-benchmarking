import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    board = []
    for _ in range(n):
        row = [int(next(it)) for _ in range(n)]
        board.append(row)
    
    row_sums = [0] * n
    col_sums = [0] * n
    
    for i in range(n):
        for j in range(n):
            row_sums[i] += board[i][j]
            col_sums[j] += board[i][j]
    
    max_weight = 0
    for i in range(n):
        for j in range(n):
            weight = row_sums[i] + col_sums[j] - 2 * board[i][j]
            if weight > max_weight:
                max_weight = weight
    
    print(max_weight)

if __name__ == "__main__":
    main()