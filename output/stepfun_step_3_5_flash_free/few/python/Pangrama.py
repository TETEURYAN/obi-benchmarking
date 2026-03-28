import sys

alfabeto = set('abcdefghijlmnopqrstuvxz')
frase = sys.stdin.readline().strip()
letras = set(frase) & alfabeto
print('S' if letras == alfabeto else 'N')