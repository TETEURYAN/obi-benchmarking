import sys

data = sys.stdin.read().split()
if not data:
    exit()
n = int(data[0])
a = list(map(int, data[1:1+n]))
for i in range(1, n-1):
    if a[i-1] > a[i] and a[i] < a[i+1]:
        print("S")
        exit()
print("N")