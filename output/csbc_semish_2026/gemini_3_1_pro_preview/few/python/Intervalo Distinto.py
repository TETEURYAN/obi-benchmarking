import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])

last_seen = {}
max_len = 0
L = 0

for R in range(n):
    val = input_data[R + 1]
    if val in last_seen and last_seen[val] >= L:
        L = last_seen[val] + 1
    last_seen[val] = R
    current_len = R - L + 1
    if current_len > max_len:
        max_len = current_len

print(max_len)