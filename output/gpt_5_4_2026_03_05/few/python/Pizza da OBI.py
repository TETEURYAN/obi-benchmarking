import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

N = int(data[0])
G = int(data[1])
M = int(data[2])

total = 8 * G + 6 * M
print(max(0, total - N))