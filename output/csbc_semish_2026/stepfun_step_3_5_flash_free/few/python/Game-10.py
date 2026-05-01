import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
D = int(input_data[1])
A = int(input_data[2])

if D >= A:
    print(D - A)
else:
    print(N - A + D)