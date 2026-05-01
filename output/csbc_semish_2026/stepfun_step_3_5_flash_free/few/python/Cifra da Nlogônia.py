import sys

alfabeto = "abcdefghijklmnopqrstuvxz"
vogais = "aeiou"

# Consoantes no alfabeto
consoantes = [c for c in alfabeto if c not in vogais]

# Mapeamento de posição no alfabeto
pos = {letra: idx for idx, letra in enumerate(alfabeto)}

# Próxima consoante para cada consoante
prox_consoante = {}
for c in consoantes:
    idx = pos[c]
    for j in range(idx + 1, len(alfabeto)):
        if alfabeto[j] in consoantes:
            prox_consoante[c] = alfabeto[j]
            break
    else:
        prox_consoante[c] = c

# Vogal mais próxima para cada consoante
vogal_proxima = {}
for c in consoantes:
    idx_c = pos[c]
    melhor_vogal = None
    melhor_dist = None
    for v in vogais:
        idx_v = pos[v]
        dist = abs(idx_c - idx_v)
        if melhor_dist is None or dist < melhor_dist or (dist == melhor_dist and idx_v < pos[melhor_vogal]):
            melhor_dist = dist
            melhor_vogal = v
    vogal_proxima[c] = melhor_vogal

# Processar entrada
data = sys.stdin.read().split()
if not data:
    exit()
palavra = data[0]

saida = []
for ch in palavra:
    if ch in vogais:
        saida.append(ch)
    else:
        saida.append(ch)
        saida.append(vogal_proxima[ch])
        saida.append(prox_consoante[ch])

print(''.join(saida))