import sys

data = sys.stdin.read().split()
if not data:
    exit()
n = int(data[0])
a = list(map(int, data[1:1+n]))
total = sum(a)
metade = total // 2
soma = 0
for i in range(n):
    soma += a[i]
    if soma == metade:
        print(i+1)
        break