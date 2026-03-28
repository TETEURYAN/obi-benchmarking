import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

c = int(input_data[0])
a = int(input_data[1])

print((a + c - 2) // (c - 1))