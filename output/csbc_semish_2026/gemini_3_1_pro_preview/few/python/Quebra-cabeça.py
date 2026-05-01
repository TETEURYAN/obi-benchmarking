import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])

next_piece = {}
idx = 1
for _ in range(n):
    e = int(input_data[idx])
    c = input_data[idx+1]
    d = int(input_data[idx+2])
    next_piece[e] = (c, d)
    idx += 3

curr = 0
res = []
for _ in range(n):
    c, d = next_piece[curr]
    res.append(c)
    curr = d

print("".join(res))