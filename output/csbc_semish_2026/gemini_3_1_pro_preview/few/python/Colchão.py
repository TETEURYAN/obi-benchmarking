import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

A = int(input_data[0])
B = int(input_data[1])
C = int(input_data[2])
H = int(input_data[3])
L = int(input_data[4])

mattress = sorted([A, B, C])
door = sorted([H, L])

if mattress[0] <= door[0] and mattress[1] <= door[1]:
    print('S')
else:
    print('N')