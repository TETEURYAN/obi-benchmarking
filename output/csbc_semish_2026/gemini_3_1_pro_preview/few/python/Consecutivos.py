import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
if n == 0:
    print(0)
    exit()

max_count = 1
current_count = 1
prev = input_data[1]

for i in range(2, n + 1):
    if input_data[i] == prev:
        current_count += 1
    else:
        if current_count > max_count:
            max_count = current_count
        current_count = 1
        prev = input_data[i]

if current_count > max_count:
    max_count = current_count

print(max_count)