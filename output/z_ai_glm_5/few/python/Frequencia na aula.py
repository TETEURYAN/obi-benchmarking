import sys

input_data = sys.stdin.read().split()

if not input_data:
    exit()

# O primeiro elemento é N, o restante são os números de registro
# Convertemos os números de registro para inteiros e inserimos em um set
# O set automaticamente remove duplicatas
numeros_registro = set(map(int, input_data[1:]))

# O tamanho do set é o número de alunos únicos com presença
print(len(numeros_registro))