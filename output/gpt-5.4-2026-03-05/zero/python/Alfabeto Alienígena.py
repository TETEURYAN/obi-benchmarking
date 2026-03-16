import sys

data = sys.stdin.read().splitlines()
k, n = map(int, data[0].split())
alfabeto = set(data[1].rstrip('\n'))
mensagem = data[2].rstrip('\n')

print('S' if all(c in alfabeto for c in mensagem) else 'N')