import sys

def main():
    data = sys.stdin.read().splitlines()
    if len(data) < 7:
        return
    board = [list(row) for row in data[:7]]
    
    moves = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for r in range(7):
        for c in range(7):
            if board[r][c] != 'o':
                continue
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                tr = r + 2*dr
                tc = c + 2*dc
                if 0 <= nr < 7 and 0 <= nc < 7 and 0 <= tr < 7 and 0 <= tc < 7:
                    if board[nr][nc] == 'o' and board[tr][tc] == '.':
                        moves += 1
    print(moves)

if __name__ == "__main__":
    main()