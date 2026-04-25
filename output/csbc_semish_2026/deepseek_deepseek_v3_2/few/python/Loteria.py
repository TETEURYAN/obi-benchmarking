import sys

data = sys.stdin.read().split()
if not data:
    exit()

aposta = set(map(int, data[:6]))
sorteio = set(map(int, data[6:12]))
acertos = len(aposta & sorteio)

if acertos < 3:
    print("azar")
elif acertos == 3:
    print("terno")
elif acertos == 4:
    print("quadra")
elif acertos == 5:
    print("quina")
else:
    print("sena")