import sys

C = int(sys.stdin.readline())
A = int(sys.stdin.readline())

alunos_por_viagem = C - 1
viagens = (A + alunos_por_viagem - 1) // alunos_por_viagem

print(viagens)