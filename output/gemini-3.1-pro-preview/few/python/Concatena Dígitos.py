import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

N = int(input_data[0])
Q = int(input_data[1])

P = [0] * (N + 1)
for i in range(N):
    P[i + 1] = P[i] + int(input_data[2 + i])

idx = 2 + N
out = []
for _ in range(Q):
    L = int(input_data[idx])
    R = int(input_data[idx + 1])
    idx += 2
    
    k = R - L + 1
    S = P[R] - P[L - 1]
    ans = 11 * (k - 1) * S
    out.append(str(ans))

print('\n'.join(out))