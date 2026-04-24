import sys

data = sys.stdin.read().split()
n = int(data[0])
a = list(map(int, data[1:n+1]))

found = False
for i in range(1, n-1):
    if a[i-1] > a[i] and a[i] < a[i+1]:
        found = True
        break

print("S" if found else "N")