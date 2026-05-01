
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
    E, C, D = piece
    left_to_piece[E] = piece
    right_to_piece[D] = piece

start = left_to_piece[0]
current = start
result = []

while True:
    E, C, D = current
    result.append(C)
    if D == 1:
        break
    current = left_to_piece[D]

print(''.join(result))
