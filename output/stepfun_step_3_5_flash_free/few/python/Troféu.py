import sys

pontuacoes = list(map(int, sys.stdin.read().split()))[:5]

maior = pontuacoes[0]
i = 0
while i < 5 and pontuacoes[i] == maior:
    i += 1
trofeus = i

if i == 5:
    placas = 0
else:
    segunda = pontuacoes[i]
    j = i
    while j < 5 and pontuacoes[j] == segunda:
        j += 1
    placas = j - i

print(trofeus, placas)