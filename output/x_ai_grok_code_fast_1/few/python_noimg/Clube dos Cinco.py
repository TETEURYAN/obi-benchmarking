import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
A, B, C, D, E, F, G = map(int, input_data[1:8])

if N == G + A + B + C - D - E - F:
    print("N")
else:
    print("S")