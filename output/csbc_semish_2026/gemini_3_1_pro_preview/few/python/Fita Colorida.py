import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
tape = [int(x) for x in input_data[1:n+1]]

dist = [10**9] * n

last_zero = -10**9
for i in range(n):
    if tape[i] == 0:
        last_zero = i
    dist[i] = min(dist[i], i - last_zero)

last_zero = 10**9
for i in range(n - 1, -1, -1):
    if tape[i] == 0:
        last_zero = i
    dist[i] = min(dist[i], last_zero - i)

for i in range(n):
    if dist[i] >= 9:
        dist[i] = 9

print(*(dist))