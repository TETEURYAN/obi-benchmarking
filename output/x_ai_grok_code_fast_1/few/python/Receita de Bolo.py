import sys

input_data = sys.stdin.read().split()
A, B, C = map(int, input_data)
max_bolos = min(A // 2, B // 3, C // 5)
print(max_bolos)