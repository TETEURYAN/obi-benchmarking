import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

d = int(input_data[0])
r = d % 400
print(min(r, 400 - r))