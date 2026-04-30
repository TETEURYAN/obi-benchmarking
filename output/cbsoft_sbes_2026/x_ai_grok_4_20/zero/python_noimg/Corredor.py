
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
vidas = list(map(int, data[1:]))

max_vidas = float('-inf')
atual = 0

for v in vidas:
    atual += v
    if atual > max_vidas:
        max_vidas = atual
    if atual < 0:
        atual = 0

print(max_vidas)
