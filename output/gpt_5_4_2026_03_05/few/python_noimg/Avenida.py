import sys

data = sys.stdin.read().split()
if not data:
    exit()

d = int(data[0])
r = d % 400
print(min(r, 400 - r))