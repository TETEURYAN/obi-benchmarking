import sys

data = list(map(int, sys.stdin.read().split()))
n = data[0]

soma = 0
for i in range(1, n + 1):
    soma += data[i]
    if soma >= 1000000:
        print(i)
        break