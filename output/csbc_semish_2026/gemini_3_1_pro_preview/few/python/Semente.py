import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

F = int(input_data[0])
R = int(input_data[1])
positions = [int(x) for x in input_data[2:2+R]]

max_days = positions[0] - 1

for i in range(1, R):
    dist = (positions[i] - positions[i-1]) // 2
    if dist > max_days:
        max_days = dist

if F - positions[-1] > max_days:
    max_days = F - positions[-1]

print(max_days)