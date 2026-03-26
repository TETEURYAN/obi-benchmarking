import sys

input_data = sys.stdin.read().split()

if not input_data:
    exit()

# Converte os valores para inteiros.
# A entrada termina com 0. Como os números da sequência são positivos (>= 1),
# o 0 nunca será o maior número, então podemos aplicar max() diretamente na lista completa.
numeros = list(map(int, input_data))

print(max(numeros))