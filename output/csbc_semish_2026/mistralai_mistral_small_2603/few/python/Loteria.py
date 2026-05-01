
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    aposta = list(map(int, data[:6]))
    sorteados = list(map(int, data[6:12]))

    acertos = len(set(aposta) & set(sorteados))

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

if __name__ == "__main__":
    main()
