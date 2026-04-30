
N = int(input())

# Nenhum face pintada: cubo interno (N-2)^3, se N>2
nenhum = max(0, (N - 2) ** 3)

# Uma face pintada: 6 faces, cada uma com (N-2)^2 cubos (se N>2)
uma = 6 * max(0, (N - 2) ** 2)

# Duas faces pintadas: 12 arestas, cada uma com (N-2) cubos (se N>2)
duas = 12 * max(0, N - 2)

# Três faces pintadas: 8 cantos
tres = 8

print(nenhum)
print(uma)
print(duas)
print(tres)
