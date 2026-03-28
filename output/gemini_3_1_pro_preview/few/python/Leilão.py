import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
best_name = ""
best_value = -1

idx = 1
for _ in range(n):
    name = input_data[idx]
    value = int(input_data[idx+1])
    if value > best_value:
        best_value = value
        best_name = name
    idx += 2

if best_value != -1:
    print(best_name)
    print(best_value)