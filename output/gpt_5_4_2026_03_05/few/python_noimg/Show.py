import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

A, N, M = data[0], data[1], data[2]
idx = 3

answer = -1

for row_input_index in range(N):
    row_number = N - row_input_index
    consecutive = 0
    found = False
    for _ in range(M):
        x = data[idx]
        idx += 1
        if x == 0:
            consecutive += 1
            if consecutive >= A:
                found = True
        else:
            consecutive = 0
    if found and answer == -1:
        answer = row_number

print(answer)