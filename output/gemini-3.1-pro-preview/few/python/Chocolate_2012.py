import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

L = float(input_data[0])
pieces = 1

while L >= 2.0:
    L /= 2.0
    pieces *= 4

print(pieces)