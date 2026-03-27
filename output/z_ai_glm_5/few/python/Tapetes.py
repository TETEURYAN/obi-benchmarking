
import sys

L, N = map(int, sys.stdin.read().split())

# Para maximizar a soma das áreas (soma dos quadrados) com soma fixa dos lados,
# devemos concentrar todo o "excesso" em um único tapete.
# Estratégia: N-1 tapetes de tamanho 1x1 e 1 tapete de tamanho (L-N+1)x(L-N+1)

maior_lado = L - N + 1
resultado = (N - 1) + maior_lado * maior_lado
print(resultado)
