import sys

input_data = sys.stdin.read().split()
idx = 0
N = int(input_data[idx])
idx += 1
max_v = -1
winner = ""
for _ in range(N):
    C = input_data[idx]
    idx += 1
    V = int(input_data[idx])
    idx += 1
    if V > max_v:
        max_v = V
        winner = C
print(winner)
print(max_v)