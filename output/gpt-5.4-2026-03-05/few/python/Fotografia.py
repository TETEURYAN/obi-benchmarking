import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

A, L = data[0], data[1]
N = data[2]

best_id = -1
best_extra = None

idx = 3
photo_area = A * L

for i in range(1, N + 1):
    x = data[idx]
    y = data[idx + 1]
    idx += 2

    if (x >= A and y >= L) or (x >= L and y >= A):
        extra = x * y - photo_area
        if best_extra is None or extra < best_extra:
            best_extra = extra
            best_id = i

print(best_id)