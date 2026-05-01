
import sys
from collections import defaultdict

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    M = int(data[0])
    N = int(data[1])
    cheques = []
    index = 2
    for i in range(M):
        X = int(data[index])
        V = int(data[index+1])
        Y = int(data[index+2])
        index += 3
        cheques.append((X, V, Y))
    
    saldo = [0] * (N + 1)
    for X, V, Y in cheques:
        saldo[X] -= V
        saldo[Y] += V
    
    credores = []
    devedores = []
    for i in range(1, N + 1):
        if saldo[i] > 0:
            credores.append((i, saldo[i]))
        elif saldo[i] < 0:
            devedores.append((i, -saldo[i]))
    
    total = sum(v for _, v in credores)
    possivel = False
    
    if len(credores) > 0 and len(devedores) > 0:
        credor_maior = max(credores, key=lambda x: x[1])
        devedor_maior = max(devedores, key=lambda x: x[1])
        
        if credor_maior[1] > devedor_maior[1]:
            possivel = True
        elif credor_maior[1] < devedor_maior[1]:
            possivel = True
        else:
            if len(credores) > 1 or len(devedores) > 1:
                possivel = True
    
    print('S' if possivel else 'N')
    print(total)

if __name__ == "__main__":
    main()
