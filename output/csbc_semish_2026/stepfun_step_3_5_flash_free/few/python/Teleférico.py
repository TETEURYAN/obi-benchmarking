import sys
C, A = map(int, sys.stdin.read().split())
max_alunos = C - 1
viagens = (A + max_alunos - 1) // max_alunos
print(viagens)