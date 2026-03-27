import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
M = int(input_data[1])
matrix = []
idx = 2
for i in range(N):
    row = [int(input_data[idx + j]) for j in range(M)]
    matrix.append(row)
    idx += M

is_echelon = True
for i in range(N):
    j = 0
    while j < M and matrix[i][j] == 0:
        j += 1
    if j == M:
        for k in range(i + 1, N):
            if any(matrix[k][c] != 0 for c in range(M)):
                is_echelon = False
                break
        if not is_echelon:
            break
    else:
        for k in range(i + 1, N):
            for c in range(j + 1):
                if matrix[k][c] != 0:
                    is_echelon = False
                    break
            if not is_echelon:
                break
        if not is_echelon:
            break

if is_echelon:
    print('S')
else:
    print('N')