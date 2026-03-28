import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    L = int(next(it))
    C = int(next(it))
    A = int(next(it)) - 1
    B = int(next(it)) - 1
    
    grid = []
    for _ in range(L):
        row = [int(next(it)) for _ in range(C)]
        grid.append(row)
    
    # direções: N, S, E, W
    dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    
    # achar o primeiro vizinho preto
    start_neighbor = None
    for dr, dc in dirs:
        nr, nc = A + dr, B + dc
        if 0 <= nr < L and 0 <= nc < C and grid[nr][nc] == 1:
            start_neighbor = (dr, dc)
            break
    
    # caminhar até o fim
    prev_r, prev_c = A, B
    cur_r, cur_c = A + start_neighbor[0], B + start_neighbor[1]
    
    while True:
        # achar próximo movimento
        next_move = None
        for dr, dc in dirs:
            nr, nc = cur_r + dr, cur_c + dc
            if 0 <= nr < L and 0 <= nc < C and grid[nr][nc] == 1 and (nr, nc) != (prev_r, prev_c):
                next_move = (dr, dc)
                break
        if next_move is None:
            # fim do caminho
            break
        prev_r, prev_c = cur_r, cur_c
        cur_r += next_move[0]
        cur_c += next_move[1]
    
    print(cur_r + 1, cur_c + 1)

if __name__ == "__main__":
    main()