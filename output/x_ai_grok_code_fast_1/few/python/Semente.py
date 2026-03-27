import sys

input_data = sys.stdin.read().split()
F = int(input_data[0])
R = int(input_data[1])
positions = [int(x) for x in input_data[2:2+R]]

max_days = positions[0] - 1
max_days = max(max_days, F - positions[-1])

for i in range(R-1):
    diff = positions[i+1] - positions[i]
    max_days = max(max_days, diff // 2)

print(max_days)