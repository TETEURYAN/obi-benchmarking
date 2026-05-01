import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
energies = list(map(int, input_data[1:]))
min_e = min(energies)
max_e = max(energies)
print(2 * (max_e - min_e))