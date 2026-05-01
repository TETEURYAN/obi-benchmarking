import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
result = (n + 1) * (n + 2) // 2
print(result)