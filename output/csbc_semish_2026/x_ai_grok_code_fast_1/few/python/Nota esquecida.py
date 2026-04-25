import sys

input_data = sys.stdin.read().split()
A = int(input_data[0])
M = int(input_data[1])
B = 2 * M - A
print(B)