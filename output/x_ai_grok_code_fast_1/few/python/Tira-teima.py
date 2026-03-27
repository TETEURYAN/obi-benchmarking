import sys

data = sys.stdin.read().split()
X = int(data[0])
Y = int(data[1])
if 0 <= X <= 432 and 0 <= Y <= 468:
    print("dentro")
else:
    print("fora")