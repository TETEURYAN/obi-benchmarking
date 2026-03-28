import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
m = int(input_data[1])

min_sum = float('inf')

for j in range(m):
    current_sum = 0
    for i in range(n):
        current_sum += int(input_data[2 + i * m + j])
    if current_sum < min_sum:
        min_sum = current_sum

print(min_sum)