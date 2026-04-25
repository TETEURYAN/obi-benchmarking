import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
m = int(input_data[1])
a = [int(x) for x in input_data[2:n+2]]

moves = 0
for i in range(n - 1):
    diff = m - a[i]
    moves += abs(diff)
    a[i] += diff
    a[i+1] += diff

print(moves)