import sys

data = sys.stdin.read().split()
n = int(data[0])
a = list(map(int, data[1:n+1]))

max_sum = a[0]
current = a[0]
for i in range(1, n):
    current = max(a[i], current + a[i])
    max_sum = max(max_sum, current)

print(max_sum)