import sys

sys.setrecursionlimit(1000000)

def main():
    input = sys.stdin.readline
    n = int(input())
    i, j = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]

    visited = [[False] * n for _ in range(n)]

    # Direções considerando orientação inicial para o norte
    # Ao virar 90 graus no sentido horário, a sequência é:
    # leste, sul, oeste, norte
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def dfs(r, c):
        visited[r][c] = True
        cur = a[r][c]
        total = 1

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                if not visited[nr][nc] and a[nr][nc] >= cur:
                    total += dfs(nr, nc)
        return total

    print(dfs(i - 1, j - 1))

if __name__ == "__main__":
    main()
