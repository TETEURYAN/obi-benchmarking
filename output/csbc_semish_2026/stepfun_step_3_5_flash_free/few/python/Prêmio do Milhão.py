import sys

data = sys.stdin.read().split()
n = int(data[0])
soma = 0
for i in range(1, n+1):
    soma += int(data[i])
    if soma >= 1000000:
        print(i)
        break