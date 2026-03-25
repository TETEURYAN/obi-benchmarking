import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

T = int(input_data[0])
N = int(input_data[1])
Y = sorted(int(x) for x in input_data[2:2+N])

min_len = (Y[0] + Y[1]) / 2.0

last_len = T - (Y[-2] + Y[-1]) / 2.0
if last_len < min_len:
    min_len = last_len

for i in range(1, N - 1):
    curr_len = (Y[i+1] - Y[i-1]) / 2.0
    if curr_len < min_len:
        min_len = curr_len

print(f"{min_len:.2f}")