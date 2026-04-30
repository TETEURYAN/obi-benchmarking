
import math

C = int(input())
A = int(input())

cap_alunos = C - 1
viagens = math.ceil(A / cap_alunos)
print(viagens)
