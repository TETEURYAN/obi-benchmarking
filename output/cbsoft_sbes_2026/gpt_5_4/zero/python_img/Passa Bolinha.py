import sys

sys.setrecursionlimit(1000000)

def main():
    input = sys.stdin.readline
    N = int(input())
    I, J = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(N)]

    visited = [[False] * N for _ in range(N)]

    # Direções ao virar 90 graus no sentido horário a partir do norte:
    # leste, sul, oeste, norte
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def dfs(r, c):
        visited[r][c] = True
        v = a[r][c]
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                if not visited[nr][nc] and a[nr][nc] >= v:
                    dfs(nr, nc)

    dfs(I - 1, J - 1)

    ans = sum(sum(row) for row in visited)
    print(ans)

if __name__ == "__main__":
    main()
