import sys

data = sys.stdin.read().split()
idx = 0
A = int(data[idx]); idx += 1
L = int(data[idx]); idx += 1
N = int(data[idx]); idx += 1

best_id = -1
best_area = float('inf')

for i in range(1, N + 1):
    X = int(data[idx]); idx += 1
    Y = int(data[idx]); idx += 1
    
    fits = False
    area = float('inf')
    
    # Try without rotation
    if X >= A and Y >= L:
        fits = True
        area = min(area, X * Y)
    
    # Try with rotation (swap X and Y)
    if X >= L and Y >= A:
        fits = True
        area = min(area, X * Y)
    
    if fits:
        if area < best_area:
            best_area = area
            best_id = i

print(best_id)