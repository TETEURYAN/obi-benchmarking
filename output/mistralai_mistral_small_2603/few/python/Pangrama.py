
import sys

alfabeto = set('abcdefghijlmnopqrstuvxz')
entrada = sys.stdin.read().strip()
letras_encontradas = set()

for char in entrada:
    if char in alfabeto:
        letras_encontradas.add(char)

print('S' if letras_encontradas == alfabeto else 'N')
