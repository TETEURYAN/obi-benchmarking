import sys
input = sys.stdin.readline

def main():
    n = int(input())
    board = []
    for _ in range(n):
        row = list(map(int, input().split()))
        board.append(row)
    
    row_sum = [sum(board[i]) for i in range(n)]
    col_sum = [sum(board[i][j] for i in range(n)) for j in range(n)]
    
    max_weight = 0
    for i in range(n):
        for j in range(n):
            weight = row_sum[i] + col_sum[j] - board[i][j]
            if weight > max_weight:
                max_weight = weight
    
    print(max_weight)

main()