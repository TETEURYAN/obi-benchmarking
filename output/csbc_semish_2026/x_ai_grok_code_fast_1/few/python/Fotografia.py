import sys

input_data = sys.stdin.read().split()
idx = 0
A = int(input_data[idx])
idx += 1
L = int(input_data[idx])
idx += 1
N = int(input_data[idx])
idx += 1

best_i = -1
min_area = float('inf')

for i in range(1, N + 1):
    X = int(input_data[idx])
    idx += 1
    Y = int(input_data[idx])
    idx += 1
    for x, y in [(X, Y), (Y, X)]:
        if A <= x and L <= y:
            area = x * y - A * L
            if area < min_area or (area == min_area and (best_i == -1 or i < best_i)):
                min_area = area
                best_i = i

print(best_i)