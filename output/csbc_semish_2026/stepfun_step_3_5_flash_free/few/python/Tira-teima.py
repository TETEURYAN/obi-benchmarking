import sys

data = sys.stdin.read().split()
if not data:
    exit()

x = int(data[0])
y = int(data[1])

if 0 <= x <= 432 and 0 <= y <= 468:
    print("dentro")
else:
    print("fora")