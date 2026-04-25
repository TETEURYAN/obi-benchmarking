import sys

input_data = sys.stdin.read().split()
if input_data:
    n = int(input_data[0])
    print((n + 1) * (n + 2) // 2)