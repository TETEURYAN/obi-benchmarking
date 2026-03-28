import sys

data = list(map(int, sys.stdin.read().split()))
aposta = set(data[:6])
sorteados = set(data[6:12])

acertos = len(aposta & sorteados)

if acertos == 6:
    print("sena")
elif acertos == 5:
    print("quina")
elif acertos == 4:
    print("quadra")
elif acertos == 3:
    print("terno")
else:
    print("azar")