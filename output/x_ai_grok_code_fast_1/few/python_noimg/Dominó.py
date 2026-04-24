import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
result = ((N + 1) * (N + 2)) // 2
print(result)