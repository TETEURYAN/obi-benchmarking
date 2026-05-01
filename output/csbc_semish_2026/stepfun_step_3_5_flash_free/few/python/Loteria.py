import sys

a = list(map(int, sys.stdin.read().split()))
aposta = a[:6]
sorteio = a[6:12]
c = len(set(aposta) & set(sorteio))
if c == 6:
    print("sena")
elif c == 5:
    print("quina")
elif c == 4:
    print("quadra")
elif c == 3:
    print("terno")
else:
    print("azar")