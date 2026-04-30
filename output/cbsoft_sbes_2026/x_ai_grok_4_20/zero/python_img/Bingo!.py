
import sys

input = sys.stdin.read
data = input().split()

index = 0
N = int(data[index])
K = int(data[index + 1])
U = int(data[index + 2])
index += 3

cartelas = []
for i in range(N):
    cartela = set()
    for j in range(K):
        cartela.add(int(data[index]))
        index += 1
    cartelas.append(cartela)

sorteados = []
for i in range(U):
    sorteados.append(int(data[index]))
    index += 1

pos = [0] * (U + 1)
for i in range(U):
    pos[sorteados[i]] = i

min_turn = U + 1
winners = []

for c in range(N):
    max_pos = 0
    for num in cartelas[c]:
        max_pos = max(max_pos, pos[num])
    if max_pos < min_turn:
        min_turn = max_pos
        winners = [c + 1]
    elif max_pos == min_turn:
        winners.append(c + 1)

winners.sort()
print(' '.join(map(str, winners)))
