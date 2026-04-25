import sys

data = sys.stdin.read().split()
n = int(data[0])
k = int(data[1])
a = sorted([int(data[i+2]) for i in range(n)], reverse=True)
print(a[k-1])