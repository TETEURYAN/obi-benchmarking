import sys
data = sys.stdin.read().split()
n1, d1, v1 = int(data[0]), int(data[1]), int(data[2])
n2, d2, v2 = int(data[3]), int(data[4]), int(data[5])
t1 = d1 / v1
t2 = d2 / v2
print(n1 if t1 < t2 else n2)