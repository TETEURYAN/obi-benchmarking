import sys

# Leitura rápida da entrada
input_data = sys.stdin.read().split()

if not input_data:
    sys.exit()

# Extraindo os valores de A, B e C
A = int(input_data[0])
B = int(input_data[1])
C = int(input_data[2])

# A receita exige: 2 de farinha, 3 ovos e 5 de leite por bolo.
# O número de bolos é determinado pelo ingrediente que limita a produção.
bolos_farinha = A // 2
bolos_ovos = B // 3
bolos_leite = C // 5

# O resultado é o mínimo entre as quantidades possíveis de cada ingrediente
resultado = min(bolos_farinha, bolos_ovos, bolos_leite)

print(resultado)