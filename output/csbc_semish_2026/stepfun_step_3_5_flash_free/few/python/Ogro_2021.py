import sys

data = sys.stdin.read().split()
if not data:
    exit()
N = int(data[0])
if N <= 5:
    esquerda = 'I' * N if N > 0 else '*'
    direita = '*'
else:
    esquerda = 'I' * 5
    direita = 'I' * (N - 5)
print(esquerda)
print(direita)