import sys

data = sys.stdin.read().split()
A, B, C, H, L = int(data[0]), int(data[1]), int(data[2]), int(data[3]), int(data[4])

faces = [(A, B), (A, C), (B, C)]

result = "N"
for (x, y) in faces:
    if (x <= H and y <= L) or (y <= H and x <= L):
        result = "S"
        break

print(result)