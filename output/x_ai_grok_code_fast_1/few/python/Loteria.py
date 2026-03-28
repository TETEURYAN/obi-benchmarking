import sys

data = sys.stdin.read().split()
aposta = set(map(int, data[:6]))
sorteio = set(map(int, data[6:]))
acertos = len(aposta & sorteio)
if acertos == 3:
    print("terno")
elif acertos == 4:
    print("quadra")
elif acertos == 5:
    print("quina")
elif acertos == 6:
    print("sena")
else:
    print("azar")