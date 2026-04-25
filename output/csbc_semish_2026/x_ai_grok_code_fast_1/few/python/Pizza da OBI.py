import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
G = int(input_data[1])
M = int(input_data[2])
total = 8 * G + 6 * M
distribuido = min(N, total)
sobram = total - distribuido
print(sobram)