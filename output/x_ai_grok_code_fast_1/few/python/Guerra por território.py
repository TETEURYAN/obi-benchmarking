import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
a = list(map(int, input_data[1:]))
total = sum(a)
soma_esq = 0
for i in range(N):
    soma_esq += a[i]
    if soma_esq == total - soma_esq:
        print(i + 1)
        break