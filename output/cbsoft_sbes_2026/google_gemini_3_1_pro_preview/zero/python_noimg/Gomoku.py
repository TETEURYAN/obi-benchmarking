import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    board = []
    idx = 0
    for i in range(15):
        row = []
        for j in range(15):
            row.append(int(input_data[idx]))
            idx += 1
        board.append(row)
        
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    
    for r in range(15):
        for c in range(15):
            color = board[r][c]
            if color == 0:
                continue
            
            for dr, dc in directions:
                if 0 <= r + 4*dr < 15 and 0 <= c + 4*dc < 15:
                    if (board[r + dr][c + dc] == color and
                        board[r + 2*dr][c + 2*dc] == color and
                        board[r + 3*dr][c + 3*dc] == color and
                        board[r + 4*dr][c + 4*dc] == color):
                        print(color)
                        return
                        
    print(0)

if __name__ == '__main__':
    solve()