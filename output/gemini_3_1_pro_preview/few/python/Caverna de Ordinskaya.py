import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
m = int(input_data[1])

prev = 0
total_sum = 0

for i in range(2, n + 2):
    val = int(input_data[i])
    x = min(val, m - val)
    y = max(val, m - val)
    
    if x >= prev:
        prev = x
        total_sum += x
    elif y >= prev:
        prev = y
        total_sum += y
    else:
        print("-1")
        exit()

print(total_sum)