import sys

data = sys.stdin.read().split()
if not data:
    exit()
L = int(data[0])
k = L.bit_length() - 1
print(1 << (2 * k))