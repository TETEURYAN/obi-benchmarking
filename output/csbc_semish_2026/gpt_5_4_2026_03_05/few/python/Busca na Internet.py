import sys

data = sys.stdin.read().split()
if not data:
    exit()

t = int(data[0])
print(t * 4)