import sys

data = sys.stdin.read().split()
if not data:
    exit()

L = int(data[0])
k = 0
while L >= 2:
    L //= 2
    k += 1

print(4 ** k)