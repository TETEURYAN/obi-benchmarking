import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
k = int(input_data[1])

x = [int(i) for i in input_data[2:2+n]]
x.sort()

keep = n - k
min_diff = float('inf')

for i in range(k + 1):
    diff = x[i + keep - 1] - x[i]
    if diff < min_diff:
        min_diff = diff

print(min_diff)