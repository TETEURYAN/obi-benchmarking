import sys

permutacao = sys.stdin.readline().strip()
frase_criptografada = sys.stdin.readline().strip()
alfabeto = "abcdefghijklmnopqrstuvwxyz"
tabela = str.maketrans(permutacao, alfabeto)
print(frase_criptografada.translate(tabela))