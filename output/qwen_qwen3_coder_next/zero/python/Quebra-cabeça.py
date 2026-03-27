
n = int(input())
pieces = []
for _ in range(n):
    e, c, d = input().split()
    e, d = int(e), int(d)
    pieces.append((e, c, d))

# Construir grafo direcionado: de 'e' para 'd' com letra 'c'
# Mas como cada número aparece no máximo uma vez na esquerda e uma vez na direita,
# temos uma cadeia única.

# Vamos mapear:
# left_to_piece: para cada número que aparece na esquerda de alguma peça, qual é a peça?
# right_to_piece: para cada número que aparece na direita de alguma peça, qual é a peça?

# Mas como o número 0 aparece apenas como esquerda (da primeira peça) e o 1 aparece apenas como direita (da última peça),
# podemos percorrer a cadeia a partir do 0 até o 1.

# Alternativa: construir dicionários:
# left_map: número -> (letra, próximo_número)
# right_map: número -> (número_anterior, letra)

# Como cada número aparece no máximo uma vez na esquerda e uma vez na direita,
# temos uma sequência única.

# Vamos criar:
# next_map: para cada número x, qual é a peça que tem x na esquerda? (e então o próximo número é o número da direita dessa peça)
# prev_map: para cada número y, qual é a peça que tem y na direita? (e então o número da esquerda dessa peça é o anterior)

# Mas como temos apenas uma cadeia, podemos fazer:
# - Encontrar a peça que tem 0 na esquerda (essa é a primeira)
# - Depois, daquela peça, pegar o número da direita, e procurar a peça que tem esse número na esquerda, e assim por diante.

# Construir dicionários:
# left_to_piece: número -> (letra, direita)
# right_to_piece: número -> (esquerda, letra)

# Mas como cada número aparece no máximo uma vez na esquerda e uma vez na direita,
# podemos fazer:

left_map = {}  # esquerda -> (letra, direita)
right_map = {}  # direita -> (esquerda, letra)

for e, c, d in pieces:
    left_map[e] = (c, d)
    right_map[d] = (e, c)

# Encontrar a peça inicial: aquela cuja esquerda é 0
current = 0
result = []

# Percorrer a cadeia
while True:
    if current in left_map:
        c, next_val = left_map[current]
        result.append(c)
        current = next_val
    else:
        break

print(''.join(result))
