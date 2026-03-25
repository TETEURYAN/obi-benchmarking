import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
a = [int(x) for x in input_data[1:n+1]]

total_sum = sum(a)
half_sum = total_sum // 2

current_sum = 0
for i in range(n):
    current_sum += a[i]
    if current_sum == half_sum:
        print(i + 1)
        break