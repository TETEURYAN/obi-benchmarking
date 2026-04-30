
import sys

def main():
    data = sys.stdin.read().split()
    ptr = 0
    N = int(data[ptr])
    K = int(data[ptr+1])
    U = int(data[ptr+2])
    ptr += 3

    cartelas = []
    for _ in range(N):
        cartela = list(map(int, data[ptr:ptr+K]))
        ptr += K
        cartelas.append(set(cartela))

    sorteados = list(map(int, data[ptr:ptr+U]))
    ptr += U

    completadas = [False] * N
    vencedores = []

    for num in sorteados:
        for i in range(N):
            if not completadas[i] and num in cartelas[i]:
                cartelas[i].remove(num)
                if len(cartelas[i]) == 0:
                    completadas[i] = True
                    vencedores.append(i+1)

    vencedores.sort()
    print(' '.join(map(str, vencedores)))

if __name__ == "__main__":
    main()
