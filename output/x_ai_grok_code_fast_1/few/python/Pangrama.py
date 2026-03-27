import sys

alfabeto = set('abcdefghijlmnopqrstuvxz')
C = sys.stdin.read().strip()
letras_presentes = set()
for char in C:
    if char.isalpha():
        letras_presentes.add(char)
if letras_presentes == alfabeto:
    print('S')
else:
    print('N')