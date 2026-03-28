import sys

input_data = sys.stdin.read().split()
D = int(input_data[0])
A = int(input_data[1])
N = int(input_data[2])
diaria = D + min(N - 1, 14) * A
dias = 32 - N
total = dias * diaria
print(total)