
N = int(input())
mat = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        mat[i][j] = min(i + 1, j + 1, N - i, N - j)

for i in range(N):
    print(' '.join(map(str, mat[i])))
