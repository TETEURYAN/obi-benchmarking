
import sys

def solve():
    input_data = sys.stdin.read().split()
    if len(input_data) < 7:
        return
    board = input_data[:7]
    
    count = 0
    for i in range(7):
        for j in range(7):
            if board[i][j] == 'o':
                # up
                if i >= 2 and board[i-1][j] == 'o' and board[i-2][j] == '.':
                    count += 1
                # down
                if i <= 4 and board[i+1][j] == 'o' and board[i+2][j] == '.':
                    count += 1
                # left
                if j >= 2 and board[i][j-1] == 'o' and board[i][j-2] == '.':
                    count += 1
                # right
                if j <= 4 and board[i][j+1] == 'o' and board[i][j+2] == '.':
                    count += 1
                    
    print(count)

if __name__ == '__main__':
    solve()
