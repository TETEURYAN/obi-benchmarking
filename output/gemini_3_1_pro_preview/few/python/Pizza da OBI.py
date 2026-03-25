import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
g = int(input_data[1])
m = int(input_data[2])

total_slices = g * 8 + m * 6
print(max(0, total_slices - n))