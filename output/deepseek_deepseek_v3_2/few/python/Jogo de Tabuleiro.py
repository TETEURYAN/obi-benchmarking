import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    board = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            board[i][j] = int(next(it))
    
    for i in range(1, N):
        for j in range(1, N):
            a = board[i][j-1]
            b = board[i-1][j-1]
            c = board[i-1][j]
            whites = (a == 0) + (b == 0) + (c == 0)
            blacks = (a == 1) + (b == 1) + (c == 1)
            if whites > blacks:
                board[i][j] = 1
            else:
                board[i][j] = 0
    
    print(board[N-1][N-1])

if __name__ == "__main__":
    main()