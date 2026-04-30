
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
pieces = []
index = 1
for i in range(N):
    E = int(data[index])
    C = data[index + 1]
    D = int(data[index + 2])
    pieces.append((E, C, D))
    index += 3

left_to_piece = {}
right_to_piece = {}
for piece in pieces:
    e, c, d = piece
    left_to_piece[e] = piece
    right_to_piece[d] = piece

current_right = 0
result = []

for _ in range(N):
    piece = left_to_piece[current_right]
    e, c, d = piece
    result.append(c)
    current_right = d

print(''.join(result))
