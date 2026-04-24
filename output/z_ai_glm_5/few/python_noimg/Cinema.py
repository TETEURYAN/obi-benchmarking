import sys

def calcular_preco(idade):
    if idade < 18:
        return 15
    elif idade >= 60:
        return 20
    else:
        return 30

# Leitura rápida de toda a entrada
entrada = sys.stdin.read().split()

if not entrada:
    sys.exit()

# Convertendo para inteiros
idade1 = int(entrada[0])
idade2 = int(entrada[1])

total = calcular_preco(idade1) + calcular_preco(idade2)

print(total)