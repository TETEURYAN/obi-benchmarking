import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

L = int(input_data[0])
C = int(input_data[1])
A = int(input_data[2])
B = int(input_data[3])

r = A - 1
c = B - 1
prev_r = -1
prev_c = -1

while True:
    moved = False
    
    if r > 0 and (r - 1 != prev_r or c != prev_c) and input_data[4 + (r - 1) * C + c] == '1':
        prev_r, prev_c = r, c
        r -= 1
        moved = True
        continue
        
    if r < L - 1 and (r + 1 != prev_r or c != prev_c) and input_data[4 + (r + 1) * C + c] == '1':
        prev_r, prev_c = r, c
        r += 1
        moved = True
        continue
        
    if c > 0 and (r != prev_r or c - 1 != prev_c) and input_data[4 + r * C + (c - 1)] == '1':
        prev_r, prev_c = r, c
        c -= 1
        moved = True
        continue
        
    if c < C - 1 and (r != prev_r or c + 1 != prev_c) and input_data[4 + r * C + (c + 1)] == '1':
        prev_r, prev_c = r, c
        c += 1
        moved = True
        continue
        
    if not moved:
        break

print(f"{r + 1} {c + 1}")