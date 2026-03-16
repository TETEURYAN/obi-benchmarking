import sys

h = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = int(sys.stdin.readline())
t = int(sys.stdin.readline())

total = h * 3600 + m * 60 + s
total = (total + t) % 86400

nh = total // 3600
total %= 3600
nm = total // 60
ns = total % 60

print(nh)
print(nm)
print(ns)