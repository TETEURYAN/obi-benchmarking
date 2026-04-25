import sys

data = sys.stdin.read().split()
t1, t2, t3, t4 = map(int, data)
print(t1 + t2 + t3 + t4 - 3)