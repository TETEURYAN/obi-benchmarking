import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n = data[0]
a = data[1:1+n]

if n <= 2:
    print(1)
    sys.exit()

count = 1
prev_diff = a[1] - a[0]

for i in range(2, n):
    diff = a[i] - a[i - 1]
    if diff != prev_diff:
        count += 1
        prev_diff = diff

print(count)