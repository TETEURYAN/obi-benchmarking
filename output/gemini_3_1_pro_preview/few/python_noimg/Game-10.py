import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
d = int(input_data[1])
a = int(input_data[2])

print((d - a + n) % n)