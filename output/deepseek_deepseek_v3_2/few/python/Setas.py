import sys
sys.setrecursionlimit(300000)

def solve() -> None:
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    grid = [list(next(it)) for _ in range(n)]

    # 0 = não visitado, 1 = visitando (ciclo), 2 = seguro, 3 = não seguro
    state = [[0] * n for _ in range(n)]
    safe_count = 0

    dir_map = {
        'V': (1, 0),
        'A': (-1, 0),
        '>': (0, 1),
        '<': (0, -1)
    }

    def dfs(r: int, c: int) -> bool:
        if not (0 <= r < n and 0 <= c < n):
            return False  # sai do tabuleiro -> não seguro
        if state[r][c] == 1:
            return False  # ciclo detectado -> não seguro
        if state[r][c] != 0:
            return state[r][c] == 2  # já calculado

        state[r][c] = 1  # marcando como visitando
        dr, dc = dir_map[grid[r][c]]
        nr, nc = r + dr, c + dc
        is_safe = dfs(nr, nc)
        state[r][c] = 2 if is_safe else 3
        return is_safe

    for i in range(n):
        for j in range(n):
            if state[i][j] == 0:
                dfs(i, j)
            if state[i][j] == 2:
                safe_count += 1

    print(safe_count)

if __name__ == "__main__":
    solve()