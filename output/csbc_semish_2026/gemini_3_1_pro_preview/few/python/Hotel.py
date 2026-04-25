import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

D = int(input_data[0])
A = int(input_data[1])
N = int(input_data[2])

rate = D + (min(N, 15) - 1) * A
days = 32 - N

print(rate * days)