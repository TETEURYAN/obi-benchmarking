
import sys

input = sys.stdin.read
data = input().split()

index = 0
test_num = 1

while True:
    M = int(data[index])
    N = int(data[index + 1])
    index += 2
    if M == 0 and N == 0:
        break

    # Read matrix: M rows, N columns
    matrix = []
    for i in range(M):
        row = [int(data[index + j]) for j in range(N)]
        matrix.append(row)
        index += N

    # Read commands
    shift_x = 0  # horizontal: positive = right
    shift_y = 0  # vertical: positive = up
    while True:
        X = int(data[index])
        Y = int(data[index + 1])
        index += 2
        if X == 0 and Y == 0:
            break
        shift_x = (shift_x + X) % N
        shift_y = (shift_y + Y) % M

    # Apply shifts
    # Final image[i][j] comes from original[(i + shift_y) % M][(j - shift_x) % N]
    # Because positive shift_x (right) means content moves right, so we sample from left
    result = [[0] * N for _ in range(M)]
    for i in range(M):
        orig_i = (i + shift_y) % M
        for j in range(N):
            orig_j = (j - shift_x) % N
            result[i][j] = matrix[orig_i][orig_j]

    # Output
    print(f"Teste {test_num}")
    for row in result:
        print(' '.join(map(str, row)))
    print()
    test_num += 1
