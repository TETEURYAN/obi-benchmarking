import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    C = int(data[idx]); idx += 1
    N = int(data[idx]); idx += 1
    
    # caixas armazenam o instante em que ficam livres
    caixas = [0] * C
    atrasados = 0
    
    for _ in range(N):
        T = int(data[idx]); idx += 1
        D = int(data[idx]); idx += 1
        
        # acha o caixa que fica livre mais cedo
        livre = min(caixas)
        # tempo de início do atendimento
        inicio = max(livre, T)
        if inicio - T > 20:
            atrasados += 1
        # atualiza o caixa com o término do atendimento
        caixas[caixas.index(livre)] = inicio + D
    
    print(atrasados)

if __name__ == "__main__":
    main()