import sys

data = list(map(int, sys.stdin.read().split()))
n = data[0]
a = data[1:1 + n]

for i in range(1, n - 1):
    if a[i - 1] > a[i] < a[i + 1]:
        print("S")
        break
else:
    print("N")