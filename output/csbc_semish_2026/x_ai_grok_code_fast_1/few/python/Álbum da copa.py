import sys

input_data = sys.stdin.read().split()
idx = 0
N = int(input_data[idx])
idx += 1
M = int(input_data[idx])
idx += 1
compradas = set()
for _ in range(M):
    X = int(input_data[idx])
    compradas.add(X)
    idx += 1
faltam = N - len(compradas)
print(faltam)