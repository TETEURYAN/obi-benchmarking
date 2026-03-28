import sys

input_data = sys.stdin.read().split()
C = int(input_data[0])
N = int(input_data[1])
print(C % N)