import sys

input_data = sys.stdin.read().split()
if input_data:
    L = int(input_data[0])
    N = int(input_data[1])
    print((N - 1) + (L - N + 1) ** 2)