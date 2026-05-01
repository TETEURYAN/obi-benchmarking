import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    
    board = []
    row_sum = [0] * n
    col_sum = [0] * n
    
    for i in range(n):
        row = list(map(int, input().split()))
        board.append(row)
        s = sum(row)
        row_sum[i] = s
        for j, v in enumerate(row):
            col_sum[j] += v
    
    ans = 0
    for i in range(n):
        rs = row_sum[i]
        row = board[i]
        for j, v in enumerate(row):
            weight = rs + col_sum[j] - v
            if weight > ans:
                ans = weight
    
    print(ans)

if __name__ == "__main__":
    main()
