import sys

input_data = sys.stdin.read().split()
A = int(input_data[0])
N = int(input_data[1])
M = int(input_data[2])
rows = []
idx = 3
for i in range(N):
    row = [int(input_data[idx + j]) for j in range(M)]
    rows.append(row)
    idx += M

for i in range(N-1, -1, -1):
    fila_num = N - i
    row = rows[i]
    count = 0
    for seat in row:
        if seat == 0:
            count += 1
            if count == A:
                print(fila_num)
                sys.exit(0)
        else:
            count = 0
print(-1)