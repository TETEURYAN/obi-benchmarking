import sys
from collections import defaultdict, deque

def main():
    teste = 1
    entrada = sys.stdin.read().split()
    ptr = 0
    while True:
        E = int(entrada[ptr]) if ptr < len(entrada) else 0
        L = int(entrada[ptr+1]) if ptr+1 < len(entrada) else 0
        ptr += 2
        if E == 0 and L == 0:
            break
        grafo = defaultdict(list)
        for _ in range(L):
            x = int(entrada[ptr]) if ptr < len(entrada) else 0
            y = int(entrada[ptr+1]) if ptr+1 < len(entrada) else 0
            ptr += 2
            grafo[x].append(y)
            grafo[y].append(x)
        normal = True
        for inicio in range(1, E+1):
            visitados = set()
            fila = deque([inicio])
            visitados.add(inicio)
            while fila:
                estacao = fila.popleft()
                for vizinha in grafo[estacao]:
                    if vizinha not in visitados:
                        visitados.add(vizinha)
                        fila.append(vizinha)
            if len(visitados) != E:
                normal = False
                break
        print(f"Teste {teste}")
        teste += 1
        print("normal" if normal else "falha")
        print()

if __name__ == '__main__':
    main()