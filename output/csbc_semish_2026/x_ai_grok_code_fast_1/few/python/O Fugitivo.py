import sys

input_data = sys.stdin.read().split()
idx = 0
N = int(input_data[idx])
idx += 1
M = int(input_data[idx])
idx += 1
x, y = 0, 0
M2 = M * M
exceeded = False
for _ in range(N):
    C = input_data[idx]
    idx += 1
    D = int(input_data[idx])
    idx += 1
    if C == 'N':
        y += D
    elif C == 'S':
        y -= D
    elif C == 'L':
        x += D
    elif C == 'O':
        x -= D
    if x * x + y * y > M2:
        exceeded = True
        break
print(1 if exceeded else 0)