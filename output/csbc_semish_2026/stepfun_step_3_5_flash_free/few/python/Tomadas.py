import sys

data = sys.stdin.read().split()
if not data:
    exit()
t1, t2, t3, t4 = map(int, data[:4])
print(t1 + t2 + t3 + t4 - 3)