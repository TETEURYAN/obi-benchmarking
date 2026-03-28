
import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
values = list(map(int, input_data[1:n+1]))

max_count = 1
current_count = 1

for i in range(1, n):
    if values[i] == values[i-1]:
        current_count += 1
        if current_count > max_count:
            max_count = current_count
    else:
        current_count = 1

print(max_count)
