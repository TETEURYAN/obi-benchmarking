import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

N = int(input_data[0])
M = int(input_data[1])
P = int(input_data[2])

R = list(range(N))
C = list(range(M))

idx = 3
for _ in range(P):
    op = input_data[idx]
    a = int(input_data[idx+1]) - 1
    b = int(input_data[idx+2]) - 1
    idx += 3
    
    if op == 'L':
        R[a], R[b] = R[b], R[a]
    else:
        C[a], C[b] = C[b], C[a]

for i in range(N):
    base = R[i] * M + 1
    sys.stdout.write(" ".join([str(base + c) for c in C]) + "\n")