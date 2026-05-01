import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

A = int(input_data[0])
L = int(input_data[1])
N = int(input_data[2])

best_id = -1
min_area = float('inf')

idx = 3
for i in range(1, N + 1):
    X = int(input_data[idx])
    Y = int(input_data[idx+1])
    idx += 2
    
    if (A <= X and L <= Y) or (A <= Y and L <= X):
        area = X * Y
        if area < min_area:
            min_area = area
            best_id = i

print(best_id)