import sys

input_data = sys.stdin.read().split()
idx = 0
N = int(input_data[idx])
idx += 1
fila = [int(x) for x in input_data[idx:idx + N]]
idx += N
M = int(input_data[idx])
idx += 1
saiu = set(int(x) for x in input_data[idx:idx + M])
result = [x for x in fila if x not in saiu]
print(' '.join(map(str, result)))