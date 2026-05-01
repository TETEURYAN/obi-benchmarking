import sys

data = sys.stdin.read().split()
if not data:
    exit()
IA = int(data[0])
IB = int(data[1])
FA = int(data[2])
FB = int(data[3])

y = IB ^ FB
x = IA ^ FA ^ y
print(x + y)