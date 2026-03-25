import sys
sys.setrecursionlimit(1000000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    L = int(next(it))
    C = int(next(it))
    P = int(next(it))
    black = [[False] * (C + 2) for _ in range(L + 2)]
    for _ in range(P):
        x = int(next(it))
        y = int(next(it))
        black[x][y] = True
    
    # Representação do tabuleiro: 0=vazio, 1=preto, 2=branco
    board = [[0] * (C + 2) for _ in range(L + 2)]
    for i in range(1, L + 1):
        for j in range(1, C + 1):
            if black[i][j]:
                board[i][j] = 1
    
    best = 0
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    
    def can_place_white(r, c):
        if board[r][c] != 0:
            return False
        # Pelo menos um vizinho preto
        has_black = False
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if board[nr][nc] == 1:
                has_black = True
                break
        if not has_black:
            return False
        # Nenhum vizinho branco
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if board[nr][nc] == 2:
                return False
        return True
    
    def backtrack(pos, placed):
        nonlocal best
        if pos > L * C:
            best = max(best, placed)
            return
        
        r = (pos - 1) // C + 1
        c = (pos - 1) % C + 1
        
        # Opção 1: não colocar nada nesta casa
        backtrack(pos + 1, placed)
        
        # Opção 2: colocar branco se possível
        if can_place_white(r, c):
            board[r][c] = 2
            backtrack(pos + 1, placed + 1)
            board[r][c] = 0
    
    backtrack(1, 0)
    print(best)

if __name__ == "__main__":
    solve()