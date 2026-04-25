import sys

data = sys.stdin.read().split()
if not data:
    exit()

a, b = map(int, data)

print(2 * a - b)