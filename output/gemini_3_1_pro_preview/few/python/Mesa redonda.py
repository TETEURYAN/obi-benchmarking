import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

a = int(input_data[0])
b = int(input_data[1])

pos_a = a % 3
pos_b = b % 3

if pos_a == pos_b:
    pos_b = (pos_b + 1) % 3

print(3 - pos_a - pos_b)