import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
heights = list(map(int, input_data[1:]))

min_height = min(heights)
count = sum(1 for h in heights if h == min_height)

print(count)