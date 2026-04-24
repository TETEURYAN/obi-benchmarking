import sys

data = sys.stdin.read().split()
if not data:
    exit()
n = int(data[0])
a = list(map(int, data[1:1+n]))
a.sort()
count = 0
for i in range(n-2):
    k = i+2
    for j in range(i+1, n-1):
        while k < n and a[i] + a[j] > a[k]:
            k += 1
        count += k - j - 1
print(count)