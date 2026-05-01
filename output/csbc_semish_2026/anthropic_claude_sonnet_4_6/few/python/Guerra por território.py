import sys

data = sys.stdin.read().split()
n = int(data[0])
a = list(map(int, data[1:n+1]))

total = sum(a)
left = 0
for k in range(n):
    left += a[k]
    right = total - left
    if left == right:
        print(k + 1)
        break